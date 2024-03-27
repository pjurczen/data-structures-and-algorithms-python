import heapq

class NetworkDelayTime:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # create adj list for each node adj[node] = (time, neighbour)
        adj = {}
        for i in range(n):
            adj[i] = []
        for entry in times:
            source, destination, time = entry[0], entry[1], entry[2]
            adj[source].append((time, destination))
        # add starting node to minHeap
        min_heap = []
        min_heap.append((k, 0, k))
        total_time = 0
        explored = {}
        # pull from minHeap while it's not empty
        while min_heap:
            source, time, destination = heapq.heappop(min_heap)
            # if node has been explored continue
            if destination in explored:
                continue
            # else mark node as explored
            explored[destination] = time
            total_time = max(total_time, time)
            # add all not explored neighbour of node to minHeap
            if destination in adj:
                for next_time, next_destination in adj[destination]:
                    if next_destination not in explored:
                        heapq.heappush(min_heap, (destination, time + next_time, next_destination))
        return total_time if len(explored) == n else -1

