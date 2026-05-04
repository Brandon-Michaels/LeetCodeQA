# Problem Summary:
# Maximize coins by popping balloons
# profit by popping balloon at i: nums[i - 1] * nums[i] * nums[i + 1]
# pop all balloons

# Naive Approach:
# Try every single combination/order of popping balloons
# Can be done with a recursive function
# Gets correct / optimal answer, but in exponential time/space

# Optimal Approach:
# Maximize coins by bursting balloons in an optimal order
# Solve with bottom-up 2D DP
# create dp[l][r] where:
# dp[l][r] = max coins collected from popping balloons within indices [l,r]
# recurrence relation: current value from popping balloon at i 
# + max coins of left interval + max coins of right interval

# Time-Complexity: O(n^2)
# Space-Complexity: O(n^3)
# n is length of nums array given

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # create array with 1s on boundary
        # since first and last indices missing neighbor to left/right respectively
        # neighbor calculation can treat out of bounds indices as having value 1
        unbounded_nums = [1] + nums + [1]

        # initialize dp table
        dp = [[0] * (len(nums) + 2) for _ in range(len(nums) + 2)]

        # iterate over balloons array
        # keep track of left/right pointers
        # for dp calculation
        for l in range(len(nums), 0, -1):
            for r in range(l, len(nums) + 1):
                # try all possible balloon within [l,r]
                for i in range(l, r + 1):
                    # compute current coin val, of popping balloon at i
                    curr_profit = unbounded_nums[l - 1] * unbounded_nums[i] * unbounded_nums[r + 1]
                    curr_profit += dp[l][i - 1] + dp[i + 1][r]

                    dp[l][r] = max(dp[l][r], curr_profit)
        
        return dp[1][len(nums)]


        





        