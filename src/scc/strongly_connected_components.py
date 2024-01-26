from src.scc.directed_graph import DirectedGraph


class StronglyConnectedComponents:
    def __init__(self):
        self.t = {}  # finishing times
        self.s = {}  # leaders
        self.time_counter = 0
        self.explored = {}

    def find_scc(self, graph: DirectedGraph) -> int:
        reversed_graph = graph.reversed()
        self.dfs_loop_reversed(reversed_graph)
        self.dfs_loop(graph)

        sccs = [len(j) for i,j in self.s.items()]
        sccs.sort(reverse=True)

        return sccs[0:5]

    def dfs_loop_reversed(self, graph: DirectedGraph):
        self.explored = {}
        self.time_counter = 0
        n = graph.get_nodes_count()
        for i in range(n):
            node = n - i
            if node not in self.explored:
                self.dfs_finishing_times(graph, node)

    def dfs_finishing_times(self, graph: DirectedGraph, node: int):
        self.explored[node] = 1
        for j in graph.get_arcs(node):
            if j not in self.explored:
                self.dfs_finishing_times(graph, j)
        self.time_counter += 1
        self.t[self.time_counter] = node

    def dfs_loop(self, graph: DirectedGraph):
        self.explored = {}
        self.time_counter = 0
        n = graph.get_nodes_count()
        for i in range(n):
            node = self.t[n - i]
            if node not in self.explored:
                self.dfs_leaders(graph, node, node)

    def dfs_leaders(self, graph: DirectedGraph, node: int, leader: int):
        self.explored[node] = 1
        if leader not in self.s:
            self.s[leader] = [node]
        else:
            self.s[leader].append(node)
        for j in graph.get_arcs(node):
            if j not in self.explored:
                self.dfs_leaders(graph, j, leader)

