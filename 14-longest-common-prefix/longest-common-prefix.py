class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time-Complexity: O(nm), where n = len(str), m = max(len(word in str))
        # Space-Complexity: O(1)
        
        # iterate over all words
        # check if first char matches
        # then second char, ...
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    # move to next word, don't update prefix
                    break
                
                # else check next char.
                j += 1
                
            # prefix matches, so we can update prefix
            prefix = prefix[:j]

        return prefix
            
