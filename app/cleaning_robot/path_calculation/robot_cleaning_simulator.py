from typing import List
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

    def __init__(self, starting_place: PlaceOnGrid, commands: List[dict]):
        self.current_place = starting_place
        self.commands = commands
        self.visited_places = UniquePlacesStructure()
        self.visit(starting_place)

    def visit(self, place: PlaceOnGrid):
        self.visited_places.add(place)

    def traverse_the_grid(self):
        for command in self.commands:
            steps = command["steps"]
            direction = Direction(command["direction"])
            for i in range(steps):
                next_place = get_next_place(self.current_place, direction=direction)
                self.visit(next_place)
                self.current_place = next_place

    def get_unique_places(self):
        self.traverse_the_grid()
        return len(self.visited_places)
