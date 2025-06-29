class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Naive Approach
        # O(n) time and O(n) space
        # visited = set()
        # visitedTwice = set()

        # for i in range(len(nums)):
        #     if nums[i] in visited:
        #         visitedTwice.add(nums[i])
        #     visited.add(nums[i])
        
        # for i in range(len(nums)):
        #     if nums[i] not in visitedTwice:
        #         return nums[i]

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