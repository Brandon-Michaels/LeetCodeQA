class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach
        # Use HashMap to group anagrams
        # Key: char count within each string
        # Val: List of grouped anagrams
        # Time-Complexity: O(m * n), where n is length of anagram array
        # m is length of the longest string
        # Space-Complexity: O(m * n), for storing all strings and characters

        group_anagram = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord("a")] += 1
            group_anagram[tuple(char_count)].append(s)
        
        return list(group_anagram.values())
