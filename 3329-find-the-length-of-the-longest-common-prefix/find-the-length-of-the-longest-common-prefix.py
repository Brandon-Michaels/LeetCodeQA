# Find the Length of the Longest Common Prefix

# Problem Summary
# Inputs: two integer arrays, arr1, arr2
# Task: Find the length of the longest common prefix between two integer
# arrays, pair between arr1 and arr2 (can't have longest common prefix arr2[i] arr[j])
# Constraints/complexities: numbers can't be negative, longest common prefix must be between arr1 and arr2
# no pairs within the same array
# Edge-Cases: no common prefix at all, single element arrays
# Outputs: maximum length, int, 'L' such that some number in arr1 and some number in arr2 share the decimal prefix of length 'L' 

# Naive / Non-Optimal Approach:
# Compare every pair across arrays, compute longest common prefix by comparison
# [1,2,3] [4,5,6] => (1,4), (1,5)...(3,6) => 0
# Time-Complexity: O(nmD), n is len(arr1), m is len(arr2), D is max Digits
# Space-Complexity: O(1), no extra space needed

# Approach
# Build a set of all numeric prefixes from arr1 by repeatedly truncating digits from the right
# For each number in arr2, walk its prefixes from full to shortest while keeping current digit length
# check membership in the set, update answer
# Time-Complexity: O(total digits across both arrays) => O((n + m) * D), n is len(arr1), m is len(arr2), D = max digit length
# membership checks are O(1), each number contributes only its digit count steps, removing the pairwise factor
# Space-Complexity: O(sum of digits in arr1) => O(n * D)

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # build a set of all prefixes that occur in arr1
        # a prefix is formed by truncating the number from the right
        # example => (123) => [123, 12, 1]
        prefixes = set()

        # traverse numbers in arr1
        for a in arr1:
            # Edge Case / Base-Case
            if a == 0:
                prefixes.add(0)
                continue
            x = a
            # generate all prefix truncations
            while x > 0:
                prefixes.add(x)
                x //= 10
        
        # scan arr2, check its prefixes against the set
        # to find the longest match
        best = 0

        # traverse all numbers in arr2
        for b in arr2:
            # Edge Case Handling
            if b == 0:
                if 0 in prefixes:
                    # 0 is single digit prefix
                    best = max(best, 1)
                continue
            
            x = b
            # digit length => match truncation
            k = len(str(b))
            while x > 0:
                # prefix exists
                # determine max length
                if x in prefixes:
                    if k > best:
                        best = k
                # consider shorter prefixes
                x //= 10
                # reduce digit length to match the truncation
                k -= 1

        return best

        

















        