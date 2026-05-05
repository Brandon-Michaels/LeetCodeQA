# Problem Summary:
# Return boolean (true/false) if array can be partitioned
# into two subsets s.t. sum(subset1) == sum(subset2)
# Input: array of integers
# Output: boolean (true/false)

# Naive Approach:
# Try all possible subsets recursively
# Time/Space-Complexity: Exponential (not great)

# Optimal Approach:
# 1D Dynamic Programming
# Two make two equal subsets, the only way this is possible
# is if one subset can be made that equals exactly half the total sum
# of all numbers in the array
# thus, we use the dp table to track if we can form a partition
# s.t. we have numbers that exactly equal half the sum over all elements
# if this is true, then we return true, else false
# dp[i] = true/false boolean value if we can sum to number i using elements we've seen so far
# the length of dp will be half of the sum of all the elements in nums 
# Time-Complexity: O(n * t)
# Space-Complexity: O(t), n = len(nums), t = half sum of array elements

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for n in nums:
            total += n
        
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)

        dp[0] = True

        for n in nums:
            if n > target:
                return False
            for i in range(len(dp) - 1, n - 1, -1):    
                dp[i] = dp[i] or dp[i - n]
                
        return dp[target]

