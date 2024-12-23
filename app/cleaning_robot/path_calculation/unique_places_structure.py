from collections import defaultdict
from app.cleaning_robot.path_calculation.grid_helpers import PlaceOnGrid


class UniquePlacesStructureDict:

    def __init__(self):
        self.in_memory_struct = defaultdict(list)

    def __len__(self):
        total_len = 0
        for x, y in self.in_memory_struct.items():
            total_len += len(set(y))
        return total_len

    def add(self, element: PlaceOnGrid):
        self.in_memory_struct[element.x].append(element.y)


UniquePlacesStructure = UniquePlacesStructureDict
