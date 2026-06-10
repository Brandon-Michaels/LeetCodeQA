# Problem Summary:
# Given two strings s, t, return the shortest substring of s
# that contains all characters in t (with duplicates)
# if doesn't exist, return empty string
# Inputs: two strings, s, t
# Outputs: String, substring of s containing all in t (or more) or "" if none exists
# Constraints: s,t non-empty strings

# Naive Approach:
# Check all possible substrings of s, and see if the frequency of characters in t
# are all the same in the substring of s (i.e. s can have more characters, but it must contain
# at least all the characters with same frequency as t)
# Problem: Computing all substrings takes:
# Time-Complexity: O(n^2), n = len(s)
# Space-Complexity: O(1)

# Optimal Approach:
# use two pointers, window size can be length of t
# if left ptr is not a character in t, slide
# continue sliding right pointer until all characters found from t, or end of list
# will stop when the frequency of characters in t, are exactly contained within the 
# frequency of characters in the current substring in s (window)
# make map of frequencies for t, create ptrs and window_size
# if left ptr char. not in t, increment left ptr (shrink window)
# increase right ptr. until size of t, reset for each iteration
# Strat: increase right ptr while substring char. in s isn't in t
# when found match make left == right, then shift right ptr until all char found
# Time-Complexity: O(n), n = len(s)
# Space-Complexity: O(m), m = # unique char. in s and t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # doesn't exist unless s is greater than or equal to t
        # otherwise won't be substring of t in s
        if len(t) > len(s):
            return ""
        
        # count frequencies of characters in string t
        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # keep counter of char. frequency matches
        # when char. frequency is matched between window substr. and t
        # then can increment have, when have == needed, we have a matching substr.
        # minimize this substr., increment left ptr.
        matched = 0
        count_window = {}
        min_length = float('inf')
        left = 0
        best_left = 0

        for right in range(len(s)):
            # adds next char. to window frequency map
            count_window[s[right]] = 1 + count_window.get(s[right], 0)

            # if frequency of char. in substr. in s matches freq. of char. in t
            # then increment matched by one
            if (s[right] in t) and count_window[s[right]] == count_t[s[right]]:
                matched += 1
            
            while matched == len(count_t):
                curr_length = right - left + 1
                
                if curr_length < min_length:
                    min_length = curr_length
                    best_left = left

                # shift left pointer, and remove frequency of char., since that left
                # char. no longer in window
                count_window[s[left]] -= 1

                # if moving left ptr. no longer makes the substr. valid 
                # (some char. in t no longer in substr. in s), then matched should decrement
                # this exits the while loop, i.e. frequencies of char. no longer match
                if (s[left] in t) and count_window[s[left]] < count_t[s[left]]:
                    matched -= 1

                left += 1
        
        if min_length == float('inf'):
            return ""

        return s[best_left:best_left + min_length]