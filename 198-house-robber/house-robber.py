class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach:
        # 1D DP, linear space for dp table
        # curr max += take the max of the previous house
        # and the current house + two previous
        # pass that information along through DP table
        # Time-Complexity: O(n), where n is length of nums
        # Space-Complexity: O(n), where n is length of nums, for nums in DP table

        dp = [0] * len(nums)

        if nums:
            dp[0] = nums[0]
        else:
            return 0

        for i in range(1, len(nums)):
            if i == 1:
                dp[1] = max(dp[0], nums[1])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        if len(nums) < 2:
            return dp[-1]
        
        return max(dp[-1], dp[-2])