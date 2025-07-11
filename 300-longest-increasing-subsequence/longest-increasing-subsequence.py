class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach
        # 1D-DP
        # dp[i] = LIS at i [0, i]
        # max(dp[i - 1], 1 + max(traversing list))
        # Time-Complexity: O(n^2), where n is len(nums)
        # Space-Complexity: O(n)

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)



        