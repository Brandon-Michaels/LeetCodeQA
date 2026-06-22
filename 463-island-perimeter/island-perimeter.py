class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs on island
        # count how many blocks
        # each block contributes two to perimeter
        # end blocks contribute 3 to perimeter
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(row, col):
            if row >= rows or row < 0:
                return 1
            if col >= cols or col < 0:
                return 1
            if (row, col) in visited:
                return 0
            if grid[row][col] == 0:
                return 1
            
            visited.add((row, col))
            # don't re-initiate dfs on visited 1
            grid[row][col] = 0

            perim = dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
            return perim
        
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter = dfs(i, j)

        return perimeter
