class NumberOfIslands:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        count = 0

        def dfs(row, column):
            if (min(row, column) < 0 or row == rows or column == columns 
                    or (row, column) in visited or grid[row][column] == '0'):
                return
            visited.add((row, column))
            dfs(row+1, column)
            dfs(row-1, column)
            dfs(row, column+1)
            dfs(row, column-1)

        for row in range(rows):
            for column in range(columns):
                if (row, column) not in visited and grid[row][column] == '1':
                    count += 1
                    dfs(row, column)

        return count
