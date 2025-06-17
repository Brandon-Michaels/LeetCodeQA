class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach
        # 1D DP, so dp table should be linear
        # want min cost, you either take 1 step and add cost
        # or 2 steps and add cost, and take the min of those results
        # continue, until you reach len(cost) and you reach top step
        # Time-Complexity: O(n), where n is len(cost) or dp table
        # Space-Complexity: O(n), for storing cost in dp table

        minCost = [0] * len(cost)

        for i in range(len(cost)):
            if i == 0:
                minCost[0] = cost[0]
            elif i == 1:
                minCost[1] = cost[1]
            else:
                minCost[i] += min(minCost[i - 1] + cost[i], minCost[i - 2] + cost[i])

        return min(minCost[-1], minCost[-2])

