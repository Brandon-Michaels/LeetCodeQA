# Problem Summary:
# Inputs: given 0-indexed integer array nums, int x
# Task: Find minimum absolute difference between two elements in the array
# that are at least (>=) x indices apart
# Constraints: abs(i - j) >= x, abs(nums[i] - nums[j]), 0 <= x <= nums.length
# Edge-Cases: 
# Output: Return an integer denoting the min difference between elements >= x apart

# Non-Optimal / Naive Approach:
# compare every element to every other element
# determine first if element is >= x indices apart, if so, then compare the min difference between
# elements, simple approach
# Time-Complexity: O(n^2), n is len(nums)
# Space-Complexity: O(1)

# Approach:
# Bisect Left/Right
# Time-Complexity: O(nlogn), where n is len(nums)
# Space-Complexity: O(n)

from bisect import bisect_left

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        INF = 10**20
        ans = INF

        # This list will store values from nums[0..i-x] in sorted order.
        # Invariant: before processing index i, 'sorted_vals' contains all values whose indices <= i - x.
        sorted_vals = []                       # initially empty, will grow as i increases

        # Iterate i from x to end, since no valid pair exists for i < x.
        for i in range(x, len(nums)):
            v = nums[i]                        # current value we try to match with a prior value

            # Insert nums[i - x] into the sorted list, since it just became eligible.
            # Find insertion position 'pos' for this new value using binary search in O(log n).
            new_val = nums[i - x]
            pos = bisect_left(sorted_vals, new_val)    # first index where new_val can be inserted
            # Insert at 'pos'. This preserves sorted order. List insertion is O(n) in Python.
            sorted_vals[pos:pos] = [new_val]

            # Now we want the closest value(s) in sorted_vals to v.
            # Find the first element >= v using bisect_left.
            j = bisect_left(sorted_vals, v)

            # Candidate 1: successor at index j, if it exists.
            if j < len(sorted_vals):
                # Update answer with absolute difference to successor.
                diff = abs(sorted_vals[j] - v)         # |successor - v|
                if diff < ans:
                    ans = diff

            # Candidate 2: predecessor at index j - 1, if it exists.
            if j - 1 >= 0:
                # Update answer with absolute difference to predecessor.
                diff = abs(v - sorted_vals[j - 1])     # |v - predecessor|
                if diff < ans:
                    ans = diff

            # Early exit if we found zero, since 0 is the best possible difference.
            if ans == 0:
                return 0

        return ans
        