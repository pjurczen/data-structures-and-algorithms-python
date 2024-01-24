import random
from copy import deepcopy

from src.karger_min_cut.graph import Graph
from src.karger_min_cut.vertex import Vertex, VertexKey


class KargerMinCut:
    def __init__(self, graph: Graph):
        self.graph = graph


    def find_min_cut(self) -> int:
        min = float("inf")
        for i in range(1000):
            random.seed(i)
            graph = deepcopy(self.graph)
            result = self.find_min_cut_once()
            self.graph = graph
            if result < min:
                min = result
        return min

    def find_min_cut_once(self) -> int:
        while len(self.graph.vertices) > 2:
            vertex_key_1, vertex_key_2 = self.pick_random_edge()
            self.merge(vertex_key_1, vertex_key_2)
            self.remove_self_loop(vertex_key_1)
        node = list(self.graph.vertices.values())[0]
        edges_count = list(node.neighbours.values())[0]
        return edges_count

    def merge(self, key1: VertexKey, key2: VertexKey):
        u = self.graph.vertices[key1]
        v = self.graph.vertices[key2]
        u.take_over_neighbours(v.neighbours)
        u.remove_neighbour(key2)
        self.graph.replace_neighbour(key2, key1)
        self.graph.remove_vertex(v)

    def pick_random_edge(self) -> (VertexKey, VertexKey):
        _, u = random.choice(list(self.graph.vertices.items()))
        v, _ = random.choice(list(u.neighbours.items()))
        return u.key, v

    def remove_self_loop(self, key: VertexKey):
        vertex = self.graph.get_vertex(key)
        if key in vertex.neighbours:
            del vertex.neighbours[vertex.key]