class VertexKey:

    def __init__(self, label: int):
        self.label = label

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return str(self.label)

    def __eq__(self, other):
        if not isinstance(other, VertexKey):
            return False
        return self.label == other.label

    def __hash__(self) -> int:
        return hash(self.label)

    def __lt__(self, other):
        if isinstance(other, VertexKey):
            return self.label < other.label
        return NotImplemented


class Vertex:
    def __init__(self, key: VertexKey):
        self.key = key
        self.neighbours = {}

    def __str__(self):
        return "{{key: {}, neighbours: {}}}".format(self.key, self.neighbours)

    def __repr__(self):
        return "{{key: {}, neighbours: {}}}".format(self.key, self.neighbours)

    def add_neighbour(self, neighbour: VertexKey):
        if neighbour in self.neighbours:
            self.neighbours[neighbour] += 1
        else:
            self.neighbours[neighbour] = 1

    def remove_neighbour(self, neighbour: VertexKey):
        del self.neighbours[neighbour]

    def take_over_neighbours(self, neighbours):
        for key, count in neighbours.items():
            self.add_neighbour_with_count(key, count)

    def add_neighbour_with_count(self, key: VertexKey, count: int):
        if key in self.neighbours:
            self.neighbours[key] += count
        else:
            self.neighbours[key] = count

    def replace_neighbour(self, key1: VertexKey, key2: VertexKey):
        count = self.neighbours[key1]
        del self.neighbours[key1]
        self.add_neighbour_with_count(key2, count)