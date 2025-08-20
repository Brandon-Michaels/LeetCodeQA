# Problem Summary:
# Given two integers m, n return the number of possible unique
# paths that can be taken from top-left corner to bottom-right

# Approach:
# Use 2D-DP table
# where dp[i][j] = # of ways to reach row i, col j in grid
# Recurrence relation: dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])
# base-case, dp[0][0] = 1

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # base-cases, can't go up or left, so all first row
        # and all first col = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j])
        
        return dp[m - 1][n - 1]