# Problem Summary:
# given an array of ints, nums, with sliding window of size k
# return max # in the window of size k at each time step
# Inputs: nums (list of ints), k (int # of sliding window size)
# Output: return list of max # in each sliding window in size k over nums arr

# Naive Approach:
# Was originally thinking
# iterate over window, find max, return max
# slide window, remove left element, add right
# check if right is larger than max, if so then new max
# if the current left ptr is NOT the max, this is rlly simple
# if left ptr isn't max, then shifting the window, still keeps the old max
# within the window, so it's a 1 check comparison, if the new num. at right ptr
# is less than max, return old max, else if >=, num at right ptr. becomes new max
# This would be O(n) time, O(1) space
# However, the PROBLEM is that on cases where the left is the max, then requires 
# iterating over the entire window again to find the max
# in the worst case every left ptr. is max, would be O(nk) time

# Optimal Approach(es):
# Keep list of current window in desc order, remove from front
# then just keep adding
# Time: O(nlogn), Space: O(k)

# More Optimal Deque Approach:
# Add from front/back, remove from front/back of deque in O(1) time
# so keep deque in decreasing order left to right
# add to front if new element bigger than prev., else add to back
# will create desc. order list, do this as sliding window
# when curr window == k, return front of deque, remove that element
# and then add the element to the right
# keep repeating until all elements added
# Need to only keep max elements, so if new element comes in
# that is > than old number, can remove old number
# Time-Complexity: O(n), n = len(nums)
# Space-Complexity: O(n), n = len(nums)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # init data structures
        max_num_dq = deque()
        res = []

        # trackers for window size/shifting
        left = 0

        for right in range(len(nums)):
            # add numbers until window size == k
            # we want to keep desc. order
            # check if dq not empty, we can scrap 
            # old elements, if new # is > old #
            while max_num_dq and nums[right] > nums[max_num_dq[-1]]:
                max_num_dq.pop()

            max_num_dq.append(right)

            # when max no longer in window, remove it
            if max_num_dq[0] < left:
                max_num_dq.popleft()

            # when window reaches capacity
            # return max, front of deque
            if right - left + 1 == k:
                res.append(nums[max_num_dq[0]])
                left += 1

        return res

