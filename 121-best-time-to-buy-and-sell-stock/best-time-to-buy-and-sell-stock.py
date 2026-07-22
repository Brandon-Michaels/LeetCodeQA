# Problem Summary
# given an array prices, prices[i] is price of stock on ith day, return max profit
# I/O: arr prices, return maximum profit from buying one day, selling diff. day in future, or return 0 if no profit
# Assumptions/EC: prices array non-empty, price is between 0-1000

# Naive:
# Brute force check all possible pairs of transactions
# Time-Complexity: O(n^2), n = len(prices)
# Space: O(1)

# Optimal Approach:
# Sliding Window
# left/right ptr, expand right ptr as long as we are making profit, else left == right ptr
# Time-Complexity: O(n), n = len(prices)
# Space-Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0

        # must buy and sell on diff. days
        if not prices or len(prices) == 1:
            return 0

        for r in range(1, len(prices)):
            curr_prof = prices[r] - prices[left]
            if curr_prof < 0:
                left = r
            if curr_prof > maxProfit:
                maxProfit = curr_prof

        return maxProfit
        