from collections import defaultdict
import heapq

class FindCriticalAndPseudoCriticalEdges:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        # do normal MST algorithm
        adj = defaultdict(list)
        for idx, edge in enumerate(edges):
            a = edge[0]
            b = edge[1]
            w = edge[2]
            adj[a].append((w, idx, b))
            
        explored = {0: 0}
        critical_edges_candidates = {}
        pseudo_critical_edges = []
        min_heap = []
        for w, idx, b in adj[0]:
            heapq.heappush(min_heap, (w, idx, 0, b))
        while min_heap:
            w, idx, a, b = heapq.heappop(min_heap)
            # first occurence of connecting a new node -> add to critical edges
            if b not in explored:
                explored[b] = w
                critical_edges_candidates[b] = idx
            # second occurence of connecting a node with same weight -> move from critical edge to pseudo-critical edges 
            elif explored[b] == w and b in critical_edges_candidates:
                pseudo_critical_edges.append(critical_edges_candidates[b])
                del critical_edges_candidates[b]
                pseudo_critical_edges.append(idx)
            for w_n, idx_n, b_n in adj[b]:
                heapq.heappush(min_heap, (w_n, idx_n, b, b_n))

        critical_edges = [i for i in critical_edges_candidates.values()]
        return [critical_edges, pseudo_critical_edges]
        
