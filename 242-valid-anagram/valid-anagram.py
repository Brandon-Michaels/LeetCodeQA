class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time-Complexity: O(s + t)
        # Space-Complexity: O(s)
        # Alternate sorted approach, O(slogs + tlogt) time, O(1) space
        
        # edge-case check
        if len(s) != len(t):
            return False
        
        # key: char, value: count(char)
        sCount = {}
        for c in s:
            sCount[c] = 1 + sCount.get(c, 0)
        
        for j in t:
            if j not in sCount:
                return False
            if sCount[j] == 0:
                return False
            sCount[j] -= 1

        return True