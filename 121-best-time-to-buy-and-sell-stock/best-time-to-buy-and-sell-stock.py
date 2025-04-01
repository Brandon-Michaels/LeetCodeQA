class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        # Expand right ptr as long as making profit
        # Else, left ptr == right ptr
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)

        left_ptr = 0
        right_ptr = 0
        max_profit = 0

        while (right_ptr < len(prices)):
            curr_prof = prices[right_ptr] - prices[left_ptr]
            if (curr_prof >= 0):
                max_profit = max(max_profit, curr_prof)
                right_ptr += 1
            else:
                left_ptr = right_ptr
        
        return max_profit