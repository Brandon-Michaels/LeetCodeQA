class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach:
        # Math, i should be equal to nums[i]
        # 0 == 0, 1 == 1, etc,.
        # so if res starts at len(nums)
        # i == nums[i], then i - nums[i] == 0
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res