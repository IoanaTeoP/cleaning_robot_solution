from typing import NamedTuple, Tuple, List
from enum import Enum


class PlaceOnGrid(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    north = "north"
    east = "east"
    south = "south"
    west = "west"

    def is_horizontal(self):
        return self == self.west or self == self.east

    def is_backward(self):
        return self == self.west or self == self.south


def get_travel_segment_on_a_line(
    starting_point: int, steps: int, direction: Direction
) -> Tuple[list, int]:
    if direction.is_backward():
        segment = [starting_point - steps, starting_point]
        return segment, segment[0]
    else:
        segment = [starting_point, starting_point + steps]
        return segment, segment[1]


def is_out_of_bounds(point_on_any_axis: int):
    return -100_000 > point_on_any_axis or point_on_any_axis > 100_000


def merge_intervals(intervals: List[list]) -> List[list]:
    """
    Merges intervals on a line be it X or Y.
    1. Sorts the intervals by the first boundary
    2. Goes through the list of sorted intervals and merges with the previous
        one if there is an overlap.
    :param intervals: Intervals to merge
    :return: merged intervals
    """
    intervals.sort(key=lambda x: x[0])

    sorted_merged_intervals: List[list] = []
    for interval in intervals:
        # no overlap
        if not sorted_merged_intervals or sorted_merged_intervals[-1][1] < interval[0]:
            sorted_merged_intervals.append([interval[0], interval[1]])
        else:
            # overlap
            sorted_merged_intervals[-1][1] = max(
                sorted_merged_intervals[-1][1], interval[1]
            )

    return sorted_merged_intervals


def get_unique_points_on_a_line(not_overlapping_intervals: List[list]):
    return sum(
        [interval[1] - interval[0] + 1 for interval in not_overlapping_intervals]
    )
