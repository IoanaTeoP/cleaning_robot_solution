from app.cleaning_robot.path_calculation.grid_helpers import (
    PlaceOnGrid,
    Direction,
)
from app.cleaning_robot.path_calculation.unique_places_structure import (
    PlacesStructure,
)


class RobotCleaningSimulator:
    """
    Will simulate a robot cleaning unique surfaces that it passes
    """

    def __init__(self, path: dict):
        starting_place = path["start"]
        self.current_place = PlaceOnGrid(x=starting_place["x"], y=starting_place["y"])
        self.commands = path["commands"]
        self.places = PlacesStructure()
        self.unique_places = 0
        self.traversed = False

    def traverse_the_grid(self) -> None:
        for command in self.commands:
            steps = command["steps"]
            direction = Direction(command["direction"])
            next_place = self.places.add_segment(
                start_position=self.current_place, steps=steps, direction=direction
            )
            self.current_place = next_place

    def get_unique_places(self) -> int:
        if not self.unique_places:
            self.traverse_the_grid()
            self.unique_places = self.places.compute_unique_places()
        return self.unique_places
