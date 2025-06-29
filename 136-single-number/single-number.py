class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Optimal Approach
        # Bit Manipulation
        # 0 XOR anything => anything, 0 ^ num = num
        # num ^ num = 0, reverts back to previous result
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)
        
        res = 0
        for num in nums:
            res = num ^ res
        return res

        # 0 ^ num => num
        # 0000 ^ 0011 => 0011
        # 0011 ^ 0010 => 0001 ^ 0011 = 0010
        # 0011 ^ 0011 => 0000