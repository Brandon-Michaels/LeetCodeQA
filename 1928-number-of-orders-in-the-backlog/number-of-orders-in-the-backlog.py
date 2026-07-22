import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # traverse order stream
        # create max heap for buy orders
        # create min heap for sell orders
        # if top of buy order is greater than top of sell we can fill order
        # pop off both buy / sell orders 
        # return len of both heaps at the end
        MOD = 10**9 + 7

        buy_max_heap = []
        sell_min_heap = []

        for price, amt, orderT in orders:
            # order[0] = price
            if orderT == 0:
                # try filling as many orders as possible
                while amt > 0 and sell_min_heap and sell_min_heap[0][0] <= price:
                    sell_price, sell_amt = heapq.heappop(sell_min_heap)
                    min_fill = min(amt, sell_amt)
                    amt -= min_fill


                    # if there is anything still remaining from the order at to heap
                    if sell_amt > 0:
                        heapq.heappush(sell_min_heap, (sell_price, sell_amt - min_fill))
                
                # buy order must be put onto heap or else loop will never execute
                if amt > 0:
                    heapq.heappush(buy_max_heap, (-price, amt))

            elif orderT == 1:
                while amt > 0 and buy_max_heap and -buy_max_heap[0][0] >= price:
                    buy_price, buy_amt = heapq.heappop(buy_max_heap)
                    min_fill = min(amt, buy_amt)
                    amt -= min_fill

                    # if there is anything still remaining from the order at to heap
                    if buy_amt > 0:
                        heapq.heappush(buy_max_heap, (buy_price, buy_amt - min_fill))
                
                # sell order must be put onto heap or else loop will never execute
                if amt > 0:
                    heapq.heappush(sell_min_heap, (price, amt))
        
        total_backlog_remaining = 0
        for order in buy_max_heap:
            total_backlog_remaining = (total_backlog_remaining + order[1]) % MOD

        for order in sell_min_heap:
            total_backlog_remaining = (total_backlog_remaining + order[1]) % MOD
            
        return total_backlog_remaining