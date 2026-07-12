# Problem summary:
# We need to decide whether s2 can be formed from s1 by recursively splitting
# s1 into two non empty parts and optionally swapping the two children at any split.
#
# Input:
#   s1: first string
#   s2: second string
#
# Output:
#   True if s2 is a scrambled string of s1, else False
#
# Key constraints and assumptions:
#   1. Valid scramble requires equal lengths.
#   2. If two substrings do not have the same multiset of characters, they can never match.
#   3. We assume strings are not huge, so O(n^4) style DP or memoized recursion is acceptable.
#
# Small example:
#   s1 = "great", s2 = "rgeat"
#   Split "great" as "gr" + "eat"
#   Swap inside "gr" to get "rg"
#   Keep "eat" as is
#   Result is "rgeat", so answer is True.
class Solution:
    def isScramble(self, s1, s2):
        # If lengths differ, no sequence of splits and swaps can fix that.
        if len(s1) != len(s2):
            return False

        # Cache stores answers for substring pairs so we do not recompute the same state.
        # Key is a tuple: (substring_from_s1, substring_from_s2)
        memo = {}

        def dfs(a, b):
            # If we have already solved this exact subproblem, reuse it.
            if (a, b) in memo:
                return memo[(a, b)]

            # If the substrings are already identical, they are trivially scramble matches.
            if a == b:
                memo[(a, b)] = True
                return True

            # If character counts differ, these substrings can never be transformed into each other.
            # This pruning is critical because it cuts off huge parts of the recursion tree early.
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            # Try every possible split point.
            # We only split at 1..len(a)-1 because both sides must be non empty.
            n = len(a)
            for split in range(1, n):
                # Case 1:
                # No swap at this split.
                # Left part of a must match left part of b,
                # and right part of a must match right part of b.
                if dfs(a[:split], b[:split]) and dfs(a[split:], b[split:]):
                    memo[(a, b)] = True
                    return True

                # Case 2:
                # Swap at this split.
                # Left part of a must match right part of b,
                # and right part of a must match left part of b.
                if dfs(a[:split], b[n - split:]) and dfs(a[split:], b[:n - split]):
                    memo[(a, b)] = True
                    return True

            # If no split works, this pair is not a scramble match.
            memo[(a, b)] = False
            return False

        # Solve the full strings.
        return dfs(s1, s2)