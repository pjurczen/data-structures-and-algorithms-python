from collections import defaultdict
import heapq

class FindCriticalAndPseudoCriticalEdges:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        # do normal MST algorithm
        adj = defaultdict()
        for edge in grid:
            a = edge[0]
            b = edge[1]
            w = edge[2]
            adj[a].append((w, b))
            
        critical_edges = {}
        pseudo_critical_edges = {}
        min_heap = []
        for w, b in adj[0]:
            heapq.heappush(min_heap, (w, 0, b))
        while min_heap:
            w, a, b = heapq.heappop(min_heap)
            if a not in critical_edges:                                                                             





        # first occurence of connecting a new node -> add to critical edges

        # second occurence of connecting a node with same weight -> move from critical edge to pseudo-critical edges
