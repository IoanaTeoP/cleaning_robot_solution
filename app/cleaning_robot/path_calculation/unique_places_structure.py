from collections import defaultdict
from app.cleaning_robot.path_calculation.grid_helpers import (
    PlaceOnGrid,
    Direction,
    get_travel_segment_on_a_line,
    merge_intervals,
    get_unique_points_on_a_line,
    is_out_of_bounds,
)


class PlacesStructure:
    def __init__(self):
        """
        vertical_segments = {
            x1: [[y1, y2], ..., [yn, ym]]
        }
        horizontal_segments = {
            y1: [[x1, x2], ...[xn, xm]]
        }
        """
        self.total_places = 0
        self.intersections = 0
        self.vertical_segments = defaultdict(list)
        self.horizontal_segments = defaultdict(list)

    def add_segment(
        self, start_position: PlaceOnGrid, steps: int, direction: Direction
    ):
        next_stop = (
            self._add_horizontal_segment(start_position, steps, direction)
            if direction.is_horizontal()
            else self._add_vertical_segment(start_position, steps, direction)
        )
        return next_stop

    def _add_horizontal_segment(self, start_position, steps: int, direction: Direction):
        segment, stop_position_x = get_travel_segment_on_a_line(
            start_position.x, steps, direction
        )
        if is_out_of_bounds(stop_position_x):
            return start_position
        self.horizontal_segments[start_position.y].append(segment)
        return PlaceOnGrid(x=stop_position_x, y=start_position.y)

    def _add_vertical_segment(self, start_position, steps: int, direction: Direction):
        segment, stop_position_y = get_travel_segment_on_a_line(
            start_position.y, steps, direction
        )
        if is_out_of_bounds(stop_position_y):
            return start_position
        self.vertical_segments[start_position.x].append(segment)
        return PlaceOnGrid(x=start_position.x, y=stop_position_y)

    def _compute_unique_places_on_axis(self):
        """
        The unique places on one axis is the sum of lengths of segments parallel
        to the axis.
        For both vertical and horizontals, we will merge the segments (intervals)
        and retrieve the unique places.
        :return: Number of unique places
        """
        total_places = 0
        for axis_intervals in [self.horizontal_segments, self.vertical_segments]:
            for fixed_point, segments in axis_intervals.items():
                axis_intervals[fixed_point] = merge_intervals(segments)
                unique_places = get_unique_points_on_a_line(axis_intervals[fixed_point])
                total_places += unique_places
        return total_places

    def _compute_axes_intersections(self):
        """
        Computes the intersections between segments that are on different axes.
        Segments inside the structures horizontal_segments and vertical_segments
        are sorted at this point.
                        x
                     v_s[1]
                       |
                       |
        y h_s[0]-------|---------h_s[1]
                       |
                       |
                      v_s[0]

        :return: total number of intersection points including turns.
        """
        total_intersections = 0
        # Sort also the keys of the vertical segments we compare with
        # To be able to break the loop once all next segments of the other axis
        # are above the current segment.
        vertical_segments_x = sorted(self.vertical_segments.keys())

        # For each segment, we will compare with all others, but with the exclusion
        # of the ones above it, due to the sorting
        for y, horizontal_segments in self.horizontal_segments.items():
            for horizontal_segment in horizontal_segments:
                for x in vertical_segments_x:
                    # segments are above the line
                    if x > horizontal_segment[1]:
                        break

                    if not horizontal_segment[0] <= x <= horizontal_segment[1]:
                        continue

                    # possible intersections within this batch
                    for vertical_segment in self.vertical_segments[x]:
                        if y < vertical_segment[0]:
                            break
                        if not vertical_segment[0] <= y <= vertical_segment[1]:
                            continue
                        total_intersections += 1

        return total_intersections

    def compute_unique_places(self):
        # Case when robot is stationary, hasn't moved and stayed in exactly 1 point
        if not self.horizontal_segments and not self.vertical_segments:
            return 1
        self.total_places = self._compute_unique_places_on_axis()
        self.intersections = self._compute_axes_intersections()
        return self.total_places - self.intersections
