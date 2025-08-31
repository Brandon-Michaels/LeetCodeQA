# Problem Summary
# Inputs: given array of non-negative integers height
# height[i] = height of bar with width 1
# Task: return max area of water that can be trapped between the bars
# Constraints/Complexities: heights non-negative
# Edge-Cases: empty or one bar => no water, all increasing/decreasing
# Outputs: return an integer, max area of water trapped between bars

# Naive / Non-Optimal Approach:
# Compute water at i = min(maxLeft[i] - maxRight[i]) - height[i]
# Time-Complexity: O(n), n is len(height)
# Space-Complexity: O(n), keep track of maxLeft/maxRight arrays

# Approach:
# Two pointers, left and right, track leftMax and rightMax
# The lower side limits, so when height[left] <= leftMax, use leftMax
# else use rightMax
# Time-Complexity: O(n), n is len(heights)
# Space-Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # Edge Cases
        # if fewer than three bars, no container can form
        if n < 3:
            return 0
        
        # initialize pointers to start/end of height list
        left = 0
        right = n - 1

        # track the highest wall seen so far from the left and from the right
        left_max = 0
        right_max = 0

        # accumulate trapped water and track
        water = 0

        # process until the pointers meet
        while left <= right:
            # decide which side is the limiting side
            # limiting side => min(left, right)
            if height[left] <= height[right]:
                # limiting side is left side
                # update left_max to include the current left bar
                left_max = max(left_max, height[left])
                
                # water on left is left_max - current height if positive
                water += max(0, left_max - height[left])
                left += 1
            else:
                # right limiting side
                # update right_max to include right bar
                right_max = max(right_max, height[right])

                # add water, water on right is right_max minus current height
                water += max(0, right_max - height[right])
                right -= 1

        return water

