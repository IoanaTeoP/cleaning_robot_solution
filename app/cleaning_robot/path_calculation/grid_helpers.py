from typing import NamedTuple
from enum import Enum


class PlaceOnGrid(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    north = "north"
    east = "east"
    south = "south"
    west = "west"


def get_next_place(place_on_grid: PlaceOnGrid, direction: Direction) -> PlaceOnGrid:
    """
    Taking one step in direction, method will return the next grid point.
    """
    if direction == Direction.north:
        return PlaceOnGrid(x=place_on_grid.x, y=place_on_grid.y + 1)
    elif direction == Direction.south:
        return PlaceOnGrid(x=place_on_grid.x, y=place_on_grid.y - 1)
    elif direction == Direction.east:
        return PlaceOnGrid(
            x=place_on_grid.x + 1,
            y=place_on_grid.y,
        )
    elif direction == Direction.east:
        return PlaceOnGrid(
            x=place_on_grid.x - 1,
            y=place_on_grid.y,
        )
