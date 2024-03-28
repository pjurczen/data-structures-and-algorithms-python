import heapq

class SwimInRisingWater:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        min_heap = []
        min_heap.append((grid[0][0], 0, 0))
        time = 0
        visited = set()
        while min_heap:
            elev, row, column = heapq.heappop(min_heap)
            visited.add((row, column))
            time = max(time, elev)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                new_row, new_column = row+dr, column+dc
                if (new_row, new_column) in visited or min(new_row, new_column) < 0 or new_row == n or new_column == n:
                    continue
                heapq.heappush(min_heap, (grid[new_row][new_column], new_row, new_column))

        return time

