class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach:
        # Brute-Force, find all possible subarrays, compare sums
        # O(n^2)
        # Make locally best choice, that leads to global best solution
        # if adding next number results in sol. less than max, then skip
        # repeat
        # Optimization problems are often greedy problems
        # Time-Complexity: O(n), where n is len(nums)
        # Space-Complexity: O(1)

        if not nums:
            return 0
        
        maxSum = float('-inf')
        currSum = 0
        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums)):
            if (currSum) < 0:
                currSum = 0
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum

        return maxSum