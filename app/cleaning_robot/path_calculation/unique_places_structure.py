class UniquePlacesStructure:

    def __init__(self):
        self.in_memory_set = set()

    def __len__(self):
        return len(self.in_memory_set)

    def add(self, element):
        self.in_memory_set.add(element)
