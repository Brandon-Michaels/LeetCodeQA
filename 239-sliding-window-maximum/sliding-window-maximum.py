from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)                                  # length of input
        if k == 1:                                     # trivial edge case
            return nums[:]                             # each element is its own max
        dq = deque()                                   # stores indices, values strictly decreasing
        ans = []                                       # output list of window maximums

        for i, x in enumerate(nums):
            # 1) Remove indices that fell out of the window's left bound.
            # Window left index is i - k + 1. If dq[0] < left, it is stale.
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2) Maintain decreasing order.
            # While the current value x is greater than the value at dq's tail,
            # pop tail because it can never be a max for any future window including i.
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            # 3) Push current index.
            dq.append(i)

            # 4) If we've formed the first full window (i >= k - 1),
            # the front of dq is the index of the window's maximum.
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans