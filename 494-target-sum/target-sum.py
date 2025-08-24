# Problem Summary:
# Input: given an integer array of nums and target
# for each number in array, you can either ADD or SUBTRACT it
# this creates a decision tree
# Output:
# return # of different ways you can build expression such that sum equals target

# Non-Optimal Approach:
# Recursive, traverse decision tree
# COUNT all ways where leaf nodes == target
# there are 2^n different possibilities, 2 branches up to n times
# Time-Complexity: O(2^n)
# Space-Complexity: O(2^n), where n is len(nums)

# Optimal Approach:
# Recursive, traverse decision tree
# COUNT all ways where leaf nodes == target
# there are 2^n different possibilities, 2 branches up to n times
# Time-Complexity: O(n * m)
# Space-Complexity: O(m), where n is len(nums), m is sum(nums)

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_row = defaultdict(int)
            for curr_sum, count in dp.items():
                next_row[curr_sum + num] += count
                next_row[curr_sum - num] += count
            dp = next_row

        return dp[target]
        