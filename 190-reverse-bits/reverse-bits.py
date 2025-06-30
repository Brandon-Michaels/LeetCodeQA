class Solution:
    def reverseBits(self, n: int) -> int:
        # Approach
        # & with 1, add result to new int, then left shift int
        # repeat
        # Time-Complexity: O(k), where k is bits in integer
        # Space-Complexity: O(1)

        res = 0
        r = 0
        for _ in range(0, 32):
            res = (n & 1)
            n = n >> 1
            r = r << 1
            r = r | res

        return r
