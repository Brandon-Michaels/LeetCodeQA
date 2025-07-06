class Solution:
    def countBits(self, n: int) -> List[int]:
        # Approach:
        # Use 1D-DP Approach
        # The number of ones 10 has, is 1 + number of ones 
        # 10 - 8 the MSB which is 8
        # dp[i] = how many ones number at i has in binary
        # We know the MSB changes, when 2 * MSB == i

        dp = [0] * (n + 1)
        dp[0] = 0
        msb = 1

        for i in range(1, n + 1):
            if (msb * 2 == i):
                msb = i
            dp[i] = dp[i - msb] + 1
        
        return dp

