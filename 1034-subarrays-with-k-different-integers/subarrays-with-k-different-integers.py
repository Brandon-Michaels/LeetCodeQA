# Subarrays with K Different Integers
# Return number of good subarrays of nums

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
         # Helper to count subarrays with at most K distinct integers
        def atMostK(k):
            count = defaultdict(int)  # Stores frequency of each number in window
            left = 0  # Left pointer of window
            res = 0  # Result: number of valid subarrays
            for right in range(len(nums)):
                # Add nums[right] to window
                if count[nums[right]] == 0:
                    k -= 1  # New unique integer in window
                count[nums[right]] += 1
                # Shrink window if more than k unique integers
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1  # Unique integer removed
                    left += 1
                # Add number of subarrays ending at right
                res += right - left + 1
            return res
        
        # Exactly k distinct = atMost(k) - atMost(k-1)
        return atMostK(k) - atMostK(k - 1)