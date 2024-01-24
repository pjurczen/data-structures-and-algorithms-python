from src.karger_min_cut.vertex import Vertex, VertexKey


class Graph:

    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return "Vertices: {}".format(self.vertices)

    def __repr__(self):
        return "Vertices: {}".format(self.vertices)

    def add_vertex(self, vertex: Vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key: VertexKey):
        return self.vertices[key]

    def remove_vertex(self, vertex: Vertex):
        del self.vertices[vertex.key]

    def replace_neighbour(self, key1: VertexKey, key2: VertexKey):
        for vertex in self.vertices.values():
            if key1 in vertex.neighbours:
                vertex.remove_neighbour(key1)
                if key2 not in vertex.neighbours:
                    vertex.add_neighbour(key2)
