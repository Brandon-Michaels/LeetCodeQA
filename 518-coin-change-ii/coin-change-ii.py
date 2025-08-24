# Problem Summary:
# Input: given an integer amount representing a target amount of money
# and list of unique coins
# Output: return # of distinct combinations 
# that total up to amount

# Approach:
# Top-down DP Memoization (backtrack) and save previous results 
# using cache
# Time-Complexity: O(n * a), where n is len(coins), a is amount
# Space-Complexity: O(n * a)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # cache
        # key -> value
        # (i, curr_sum) : count

        dp = {}

        def backtrack(i, curr_sum):
            if i >= len(coins) or curr_sum > amount:
                return 0

            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            
            if curr_sum == amount:
                return 1

            dp[(i, curr_sum)] = (
                # take or skip
                backtrack(i, curr_sum + coins[i]) + 
                backtrack(i + 1, curr_sum)
            )

            return dp[(i, curr_sum)]

        return backtrack(0, 0)

