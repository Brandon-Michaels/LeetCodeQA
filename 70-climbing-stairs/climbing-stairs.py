class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach
        # 1D DP
        # Time-Complexity: O(n)
        # Space-Complexity: O(n)

        count = [0] * (n + 1)

        if n <= 2:
            return n

        count[1] = 1
        count[2] = 2
        
        for i in range(3, n + 1):
            count[i] = (count[i - 1] + count[i - 2])

        return count[-1]