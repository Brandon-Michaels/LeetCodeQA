# Problem Summary:
# Given two strings s1 and s2, determine if there exists
# a substring in s2 that is a permutation of s1
# Inputs:
# given two strings, s1, and s2
# Output: return boolean True/False is s2 contains a substring permutation
# of s1
# Constraints: s1, s2 Strings of non-empty length

# Naive Solution:
# Brute-Force: check every window/substring in s2 of length s1
# and determine if every character in the window is also present in s1
# if all characters in a substring of s2 exist in s1, then permutation
# must exist
# Problem: This causes slow time-complexity, brute-force
# Time-Complexity: O(mn), m = len(s1), n = len(s2), iterate over 
# Space-Complexity: O(1)

# Optimal Solution:
# Sliding window
# we know length of shorter substr
# so if there is window of len(short substr) and permutation
# which means frequency of all char. in substring in s2 are exactly in s1
# return true, if not we can slide the window forward
# this will allow us to iterate once over the length of s2
# Time-Complexity: O(n), n is max length of two strings
# Space-Complexity: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency maps for s1 and the current window in s2
        s1_count = {}
        window_count = {}

        # Build frequency count for s1
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        left = 0
        right = 0
        window_size = len(s1)

        for right in range(len(s2)):
            # build frequency map of window
            # must start by adding new right char
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # if window is too large, must remove char. from left
            # and shift window
            # right - left + 1 > window
            if (right - left + 1) > window_size:
                window_count[s2[left]] -= 1

                # must remove char from window map if count == 0
                # otherwise hashmap comparison won't work
                # b/c length mismatch
                if window_count[s2[left]] == 0:
                    window_count.pop(s2[left])

                left += 1

            # continue expanding window until window is s1 length
            # right - left + 1 == window_size
            if (right - left + 1) == window_size:
                if window_count == s1_count:
                    return True
        
        return False
