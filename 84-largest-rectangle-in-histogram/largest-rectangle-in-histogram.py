# Problem Summary:
# Inputs: array of ints, heights
# Outputs: int of largest rectangle area formed by histogram (bars)
# Consraints: heights is non-empty, height[i] >= 0

# Naive Approach:
# For every bar, extend rectangle as far left/right as it can go (<= curr. height)
# this gives the maximum rectangle per bar, just return overall highest max
# Time-Complexity: O(n^2), n = len(heights)
# Space-Complexity: O(1)

# Optimal Approach:
# for smaller bar on right side using a monotonic increasing stack
# iterate left to right, append elements on stack, when we run into smaller bar
# we no longer can append elements, we've hit our max area we can "spread" our rectangle to
# so at this point we must pop off height from the stack and compute bounds + max area
# and calculate height as: curr_height * (right_bound - left_bound + 1)
# Store index and height on stack, when pop element extend element start 
# as far back as how many elements you just popped off the stack
# This is an O(1) computation using stack, repeat for all n heights in O(n) time
# Time-Complexity: O(n), n = len(heights)
# Space-Complexity: O(n), n = len(heights)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curr_area = 0
        max_area = 0

        # append height of 0 to heights
        # so we always pop all elements off of stack
        heights.append(0)

        # python arrays can act as stacks, just append/pop as normal and it auto
        # removes from back which creates LIFO structure
        stack = []
        for i in range(len(heights)):
            # keep track of current start
            start = i
            while stack and heights[i] < stack[-1][1]:
                # pop top element (can't extend any further)
                index, height = stack.pop()
                curr_area = height * (i - index)
                max_area = max(curr_area, max_area)
                
                # curr bar must be less than all before bc of while loop cond.
                # so we can always extend curr. bar back to last popped off bar index
                start = index

            # stack tuple: (index, height)
            stack.append((start, heights[i]))
            
        return max_area