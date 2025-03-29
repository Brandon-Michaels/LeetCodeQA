class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two-Pointer Approach
        # Time-Complexity: O(n), Space-Complexity: O(n), 
        # where n is length of s

        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s)

        left = 0
        right = len(clean_s) - 1

        clean_s = clean_s.lower()

        while (left < right):
            if (clean_s[left] != clean_s[right]):
                return False
            left += 1
            right -= 1
    
        return True