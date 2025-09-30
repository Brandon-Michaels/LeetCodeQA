from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        residue_count = defaultdict(int)
        for num in nums:
            residue = num % value
            residue_count[residue] += 1
        
        mex = 0
        while True:
            residue = mex % value
            if residue_count[residue] > 0:
                residue_count[residue] -= 1
                mex += 1
            else:
                return mex
        