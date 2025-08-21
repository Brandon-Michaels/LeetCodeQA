# Problem Summary:
# Given two integers m, n return the number of possible unique
# paths that can be taken from top-left corner to bottom-right

# Approach:
# Use 2D-DP table
# where dp[i][j] = # of ways to reach row i, col j in grid
# Recurrence relation: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
# base-case, dp[0][0] = 1

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # base-cases, can't go up or left, so all first row
        # and all first col = 1
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        
        return dp[m - 1][n - 1]
        

        