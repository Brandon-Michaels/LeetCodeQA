class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach:
        # 2D DP
        # Base-Cases: dp[0][0] = T, one char. always palindrome
        # dp[i][j] = whether the string is a palindrome up to i, j
        # check curr. char to end char. and see if they match
        # curr. char = i, j = i + length of curr. max substr.
        # Time-Complexity: O(n^2) to fill dp table, where n is len(s)
        # Space-Complexity: O(n^2), where n is len(s)

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxLength = 1
        res = s[0]

        if not s:
            return ""
        if n == 1:
            return s

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # if curr. char. match and prev. str was palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > maxLength:
                        res = s[i:j+1]
                        maxLength = j - i + 1
        
        return res
        