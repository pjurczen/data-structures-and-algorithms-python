from collections import defaultdict
import heapq

class PathWithMaximumProbability:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = defaultdict(lambda: [])
        for edge, prob in zip(edges, succProb):
            adj[edge[0]].append((prob, edge[1]))
            adj[edge[1]].append((prob, edge[0]))
        min_heap = []
        min_heap.append((-1, start_node))
        visited = set()
        while min_heap:
            prob, node = heapq.heappop(min_heap)
            prob = -1*prob
            if node == end_node:
                return prob
            if node in visited:
                continue
            visited.add(node)
            for next_prob, next_node in adj[node]:
                heapq.heappush(min_heap, (-1*prob*next_prob, next_node))

        return 0

