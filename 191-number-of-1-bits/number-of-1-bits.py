class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach
        # and with 1, if it's also 1 then increment counter
        # right shift
        # Time-Complexity: O(k), where k is bit length of int in OS
        # Space-Complexity: O(1)

        res = 0
        count = 0
        while n != 0:
            res = (n & 1)
            if res == 1:
                count += 1
            n = n >> 1

        return count