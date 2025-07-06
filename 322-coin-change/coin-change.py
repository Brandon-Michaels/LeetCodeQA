class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Approach
        # 1D DP
        # dp[i] = min # of coins to build up to coin of amount i
        # Time-Complexity: O(n * t), where n is len(coins)
        # Space-Complexity: O(t), where t is amount

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1