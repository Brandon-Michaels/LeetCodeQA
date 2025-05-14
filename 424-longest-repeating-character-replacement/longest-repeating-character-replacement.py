class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Intuition:
        # k gives a buffer, longest substring w/ up to k distinct char
        # window size - occurrences of most often occuring char = # replacements we need
        # # replacements <= k keep going, else shrink left window size
        # Time-Complexity: O(n), where n is size of s
        # Space-Complexity: O(n), keep hashmap of distinct characters to count

        left = 0
        char_map = {} # char : count(char)
        max_len = 0
        curr_len = 0

        for right in range(0, len(s)):
            char_map[s[right]] = 1 + char_map.get(s[right], 0)
            while ((right - left + 1) - max(char_map.values()) > k):
                char_map[s[left]] -= 1
                left += 1
                curr_len -= 1
            
            curr_len += 1
            max_len = max(max_len, curr_len)
            
        return max_len