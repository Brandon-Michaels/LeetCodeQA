class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach:
        # 1D DP
        # if you use first element, you can't use the last element (vice-versa)
        # otherwise same approach as before
        # Time-Complexity: O(n), where n is len(nums)
        # Space-Complexity: size of dp table, n = len(nums)

        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)

        if not nums:
            return 0

        # exclude first element
        for i in range(1, len(nums)):
            if i == 1:
                dp1[1] = nums[1]
            elif i == 2:
                dp1[2] = max(dp1[1], nums[2])
            else:
                dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        # exclude last element
        for i in range(0, len(nums) - 1):
            if i == 0:
                dp2[0] = nums[0]
            elif i == 1:
                dp2[1] = max(dp2[0], nums[1])
            else:
                dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        if len(nums) == 1:
            return nums[0]

        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])
        
