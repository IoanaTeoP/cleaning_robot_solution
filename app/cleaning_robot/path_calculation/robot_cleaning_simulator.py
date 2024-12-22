from app.cleaning_robot.path_calculation.grid_helpers import (
    PlaceOnGrid,
    Direction,
    get_next_place,
)
from app.cleaning_robot.path_calculation.unique_places_structure import (
    UniquePlacesStructure,
)


class RobotCleaningSimulator:
    """
    Will simulate a robot cleaning unique surfaces that it passes
    """

    def __init__(self, path: dict):
        starting_place = path["start"]
        self.current_place = PlaceOnGrid(x=starting_place["x"], y=starting_place["y"])
        self.commands = path["commands"]
        self.visited_places = UniquePlacesStructure()
        self.visit(self.current_place)

    def visit(self, place: PlaceOnGrid) -> None:
        self.visited_places.add(place)

    def traverse_the_grid(self) -> None:
        for command in self.commands:
            steps = command["steps"]
            direction = Direction(command["direction"])
            for i in range(steps):
                next_place = get_next_place(self.current_place, direction=direction)
                self.visit(next_place)
                self.current_place = next_place

    def get_unique_places(self) -> int:
        self.traverse_the_grid()
        return len(self.visited_places)
