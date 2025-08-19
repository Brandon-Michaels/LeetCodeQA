# Problem Summary;
# Given two strings, text1 and text2, return the
# length of the LCS between the two if exists, else return 0

# Approach:
# USE 2D-DP, where dp[i][j] = LCS up to char. i in str 1 and char. j in str2
# this creates a memoized approach, so we don't need to constantly re-calculate
# best approach, this considerably saves us exponential time-complexity
# recurrence relation: if chars. match, very simply take 1 + dp[i - 1][j - 1] 
# or essentially (dp of previous), if chars. DON'T match, then we either
# expand our dp on the left or right string, because we don't know which is better
# we take the maximum of both
# repeat until both strings traversed
# Time-Complexity: O(m * n), where m is len(text1), n is len(text2)
# Space-Complexity: O(m * n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # traverse both strings
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # if chars. match extend dp
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = (1 + dp[i - 1][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return (dp[len(text1)][len(text2)])