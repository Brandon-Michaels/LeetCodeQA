class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Approach
        # Add current substring to set, if curr char alr in set, reset window
        # else expand window while keeping track of max substr size
        # Time-Complexity: O(n), where n is size of s
        # Space-Complexity: O(m), where m is the longest substring length

        left = 0
        max_len = 0
        curr_len = 0
        longest_substr = set()

        for right in range(0, len(s)):
            while (s[right] in longest_substr):
                longest_substr.remove(s[left])
                left += 1
                curr_len -= 1
            longest_substr.add(s[right])
            right += 1
            curr_len += 1
            max_len = max(max_len, curr_len)
            
        return max_len