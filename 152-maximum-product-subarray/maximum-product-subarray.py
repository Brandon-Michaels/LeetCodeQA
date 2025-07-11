class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach
        # 1D-DP
        # dp[i] = max contiguous sub-array product so far up to i
        # Base-Case: [] => -1, [i] => nums[i]
        # Recurrence: dp[i] = max(dp[i - 1], nums[i] * nums[i - 1])
        # Time-Complexity: O(n), where n is len(nums)
        # Space-Complexity: O(n), for n nums in dp table

        # Or kadane's Algo. and O(1) space

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # return dp[-1]

        # greedy-approach

        currMin, currMax = 1, 1
        maxProd = nums[0]

        for i in range(len(nums)):
            tmpMax = currMax * nums[i]
            tmpMin = currMin * nums[i]
            currMax = max(tmpMax, tmpMin, nums[i])
            currMin = min(tmpMax, tmpMin, nums[i])
            maxProd = max(maxProd, currMax)
        
        return maxProd
