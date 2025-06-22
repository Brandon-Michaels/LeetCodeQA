class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach:
        # DFS on the grid
        # Visit all 4 directions, if curr. element is == 1 AND
        # all 4 directions are == 0, then we know curr. is island
        # else, if any dir. is 1, then not island, but if curr == 1
        # and all non-visited dir. == 0, then also island
        # if curr == 0, we can skip comparisons completely
        # Time-Complexity: O(m * n), m is rows, n is cols
        # Space-Complexity: O(m * n), for recursive dfs stack

        rows = len(grid)
        cols = len(grid[0])
        countIslands = 0

        def dfs(row, col):
            # stay in-bounds
            if row >= rows or row < 0:
                return
            if col >= cols or col < 0:
                return
            if grid[row][col] == "0":
                return
            
            # prevent visiting same island again
            grid[row][col] = "0"

            # visit all 4 directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    countIslands += 1

        return countIslands