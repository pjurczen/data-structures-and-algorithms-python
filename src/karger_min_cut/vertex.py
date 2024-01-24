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
        self.neighbours[neighbour] = 1

    def remove_neighbour(self, neighbour: VertexKey):
        del self.neighbours[neighbour]