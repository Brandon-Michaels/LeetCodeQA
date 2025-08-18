# Problem Summary:
# Given an array of intervals, where intervals[i] = [start_i, end_i],
# merge overlapping intervals, return array of non-overlapping merged
# intervals

# Approach
# Sort intervals array by start time
# Use the heuristic:
# if curr_end_time >= next_start_time, then there is an overlapping interval
# merge these intervals by appending the curr_start time and next_end time
# to a new merged interval array
# Time-Complexity: O(nlogn) for sorting, where n is length of intervals array
# Space-Complexity: O(n) for extra space required for new merged interval array

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start times
        intervals.sort(key=lambda x:x[0])
        merged_intervals = [intervals[0]]

        # traverse intervals
        for start, end in intervals:
            prevEnd = merged_intervals[-1][1]

            # merge
            if start <= prevEnd:
                merged_intervals[-1][1] = max(prevEnd, end)
            else:
                merged_intervals.append([start, end])
           

        return merged_intervals
        