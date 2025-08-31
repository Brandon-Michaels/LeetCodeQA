# Problem Summary:
# Inputs: given a string s
# Task: rearrange the characters of s, so NO two adjacent characters same
# Constraints: string of lower-case english letters 
# Edge-Cases: empty string, single char
# Outputs: return string rearrangement of s, or "" if not possible

# Naive / Non-Optimal Approach
# greedy scan and swap whenever res[-1] == next_char (neighboring chars match)
# might search linearly, worst case repeated scans lead to O(n^2) time
# many nested loops here

# Approach:
# Greedy with a max heap by remaining frequency
# Always place the two most frequeny different chars next
# aaaaabbbbbcc, ababababababcab
# Early impossibility check: maxCount > ((n + 1) // 2)
# Time-Complexity: O(nlogk), n is len(s), k is distinct chars
# Space-Complexity: O(k)

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # count occurrences of each character
        # freq[c] => how many times c appears
        freq = Counter(s)

        # Edge Case checks
        n = len(s)
        if not s:
            return ""
        if (max(freq.values()) > (n + 1) // 2):
            # if any character is too frequent
            return ""

        # Build a max heap by using negative counts
        # heapq => min heap
        # each entry (-count, char), so the most frequent char pops first
        heap = [(-cnt, c) for c, cnt in freq.items()]

        # heapify => arrange list into valid heap
        heapq.heapify(heap)

        res = []

        # track the previously used char with remaining count
        prev_cnt = 0
        prev_char = ""

        # keep placing the most frequent available character
        # that differs from the previous
        while heap:
            # removes char with largest remaining count
            count, c = heapq.heappop(heap)

            # if previous char still has remaining count
            # push it back so we never place it adjacently
            if prev_cnt < 0:
                # reintroduce the prior char as a candidate
                heapq.heappush(heap, (prev_cnt, prev_char))

            # place current char in str
            res.append(c)
            
            # count is negative, adding one moves it to zero
            count += 1

            # store for next iteration
            prev_cnt = count
            prev_char = c

        # join the res list into a string
        # [a, b, c, d, b, a] => "abcdba"
        ans = "".join(res)

        return ans

