class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_arc(self, i: int, j: int):
        if i in self.nodes:
            self.nodes[i].append(j)
        else:
            self.nodes[i] = [j]

    def get_nodes_count(self) -> int:
        return len(self.nodes)

    def get_arcs(self, tail):
        if tail not in self.nodes:
            return []
        return self.nodes[tail]
