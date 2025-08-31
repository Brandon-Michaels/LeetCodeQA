# Problem Summary
# Inputs: array nums, integer k
# Task: return # of good subarrays
# subarray is good if it contains at least k pairs
# of indices (i, j) with i < j AND arr[i] == arr[j]
# Constraints/Complexities: could be given large n, values integers
# nums array containing integers
# Edge-Cases: k == 0 gives all subarrays, all distinct values
# Outputs: return int count of good subarrays

# Non-Optimal/Naive Approach:
# Enumerate all subarrays and count pairs via a frequency map per subarray
# Time-Complexity: O(n^2)
# Space-Complexity: O(u) for counts of all pairs

# Optimal Approach
# Sliding window with pair counting
# Maintain window [l, r], map freq and pairs inside the window
# when we extend to r with value x, new equal pairs formed equals current freq[x]
# if pairs >= k, any extension to the right will remain good, so for the current r
# there are n - r good subarrays starting at any l in [0..l], after we shrink left as little as needed
# shrink from the left while pairs >= k, pairs -= freq[nums[l]] - 1
# Time-Complexity: O(n), n is len(nums), each index moves at most once
# Space-Complexity: O(u), u is number of distinct elements in the current window

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # edge case
        if k == 0:
            return (n * (n + 1) // 2)
        
        # frequency of values in the current window
        freq = defaultdict(int)
        pairs = 0
        l = 0
        res = 0

        # expand the window by moving right pointer
        for r, x in enumerate(nums):
            # add x pairs with all previous x in window
            # include x in window
            pairs += freq[x]
            freq[x] += 1

            # while window has at least k pairs, it's valid
            # so each shift of l adds (n - r) good subarrays
            while pairs >= k:
                res += (n - r)
                # value leaving from left
                left_val = nums[l]
                # remove occurrence from window
                freq[left_val] -= 1
                pairs -= freq[left_val]
                l += 1

        return res