# Problem Summary:
# Given integer array prices, where prices[i] is price 
# of NeetCoin on the ith day, return max profit you can achieve

# Approach:
# Cooldown period of at least one day, can't buy immediately after
# you sell, so essentially integrate adjacency constraint
# 2D-DP table, where dp[i][0] = curr max profit up to 
# day i where we do NOT currently own the coin
# dp[i][1] = curr max profit up to day i where we do OWN
# the coin
# recurrence relation: dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
# simply return the max(dp[len(prices) - 1][0], dp[len(prices) - 1][1])
# Time-Complexity: O(n), where n is len(prices)
# Space-Complexity: O(n)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]

        # base-cases:
        if not prices or len(prices) == 1:
            return 0
        
        dp[0][1] = -prices[0]
        
        for i in range(1, len(prices)):
            # sell if profit, else hold
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            # buy if not owned and cooldown, else hold
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        
        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][1])