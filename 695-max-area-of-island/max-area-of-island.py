class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Approach
        # Same as num. islands, except keep a counter for the amount
        # of cells we trace through within each group
        # return that from the DFS function
        # and compare if that max is any better than what we have already
        # Time-Complexity: O(m * n) where is m is len(rows), n is len(cols)
        # Space-Complexity: O(m * n), size of stack

        rows = len(grid)
        cols = len(grid[0])
        currMax = 0
        maxSum = 0

        def dfs(row, col):
            # stay in-bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0
            
            # mark visited
            grid[row][col] = 0

            return 1 + (dfs(row + 1, col) + dfs(row - 1, col) + 
                        dfs(row, col + 1) + dfs(row, col - 1))
    
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    currMax = dfs(i, j)
                    maxSum = max(maxSum, currMax)

        return maxSum