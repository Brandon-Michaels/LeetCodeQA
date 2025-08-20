# Problem Summary:
# Given two strings, word1 and word2
# return min number of operations to make word1 == word2

# Approach:
# 2D-DP approach
# dp[i][j] = curr edit distance of words up to char. i in word1 and
# char. j in word2
# if prev. characters match => increment both pointers
# Recurrence Relation:
# if char. don't match => 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
# Time-Complexity: O(n * m), same idea here, must traverse n and m respectively
# Space-Complexity: O(n * m), where n is len(word1), m is len(word2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Initialize base-cases

        for i in range(len(word1) + 1):
            dp[i][0] = i
        
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # insertion, deletion, substitution
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        
        return dp[len(word1)][len(word2)]