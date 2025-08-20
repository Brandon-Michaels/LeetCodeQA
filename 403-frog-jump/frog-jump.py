# Problem Summary:
# Given list of stone positions in ascending order, determine if frog can 
# cross river by landing on last stone (last index), initially frog is on first stone
# and makes jump of 1, return if frog can reach last stone

# Approach:
# Use DP table containing HashMap
# HashMap will be => key: stone, value: set containing jump dist frog made to reach that stone
# Space-Complexity:
# Time-Complexity:

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone : set() for stone in stones}
        # base-case
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:
                for jump_dist in [jump - 1, jump, jump + 1]:
                    if jump_dist > 0 and (stone + jump_dist) in dp:
                        dp[stone + jump_dist].add(jump_dist)
        
        return len(dp[stones[-1]]) > 0
