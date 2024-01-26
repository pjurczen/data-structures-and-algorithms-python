class DirectedGraph:
    def __init__(self):
        self.arcs = []
        self.nodes = {}

    def add_arc(self, i: int, j: int):
        self.arcs.append((i, j))
        if i in self.nodes:
            self.nodes[i].append(j)
        else:
            self.nodes[i] = [j]

    def reversed(self):
        reversed_graph = DirectedGraph()
        for i, j in self.arcs:
            reversed_graph.add_arc(j, i)
        return reversed_graph

    def get_nodes_count(self) -> int:
        return len(self.nodes)

    def get_arcs(self, tail):
        return [j for i, j in self.arcs if i == tail]
