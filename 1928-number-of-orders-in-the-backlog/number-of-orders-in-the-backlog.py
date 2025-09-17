# Problem Summary:
# given list of orders (buy/sell, price, amount), simulate order book
# return orders left in backlog
# Inputs: orders 2D array, orders[i] = [price, amount, orderType]
# price >= 0, amount >= 0, orderType == 0 for buy, 1 == for sell orders 
# Task: match buy/sell orders with highest/lowest buy/sell price
# Constraints: no NEGATIVE price or negative amount
# Outputs: return length of order book backlog % (10^9 + 7)

# Naive / Non-Optimal Approach:
# Use lists for buy/sell backlog
# Scan linearly for matches
# Every time requires O(n^2) comparisons, N = len(orders)

# Optimal Approach:
# Use heaps for buy (max-heap), sell (min-heap)
# O(logN) matching, heaps allow us to access the best match in O(logN) time
# orders processed efficiently
# Time-Complexity: O(nlogn), n = len(orders)
# Space-Complexity: O(n)

import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 10**9 + 7

        # max-heap for buy orders
        buy_heap = []
        
        # min-heap for sell orders
        sell_heap = []

        # process each order
        for price, amount, orderType in orders:
            # determine if order == buy/sell
            if orderType == 0:
                # buy order, match with lowest sell
                # (buy low, sell high)
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    # matched sell order to our buy
                    sell_price, sell_amount = heapq.heappop(sell_heap)
            else:
                # sell order, match with highest buy
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_heap)


import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        MOD = 10**9 + 7  # Modulo for final result
        
        # Max-heap for buy orders (invert price for max-heap)
        buy_heap = []
        # Min-heap for sell orders
        sell_heap = []
        
        # Process each order
        for price, amount, orderType in orders:
            if orderType == 0:
                # Buy order: match with lowest sell
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_heap)
                    # Find min amount to match
                    match = min(amount, sell_amount)
                    amount -= match
                    sell_amount -= match
                    # If sell order still has amount, push back
                    if sell_amount > 0:
                        heapq.heappush(sell_heap, (sell_price, sell_amount))
                # If not fully matched, add remaining buy to heap
                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))
            else:
                # Sell order: match with highest buy
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_heap)
                    match = min(amount, buy_amount)
                    amount -= match
                    buy_amount -= match
                    if buy_amount > 0:
                        heapq.heappush(buy_heap, (buy_price, buy_amount))
                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))
        
        # Sum all remaining orders in both heaps
        total = 0
        for _, amt in buy_heap:
            total = (total + amt) % MOD
        for _, amt in sell_heap:
            total = (total + amt) % MOD
        return total



        