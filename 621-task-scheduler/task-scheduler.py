# Problem Summary:
# Inputs: given an array of CPU tasks, tasks
# tasks[i] => "A-Z", given integer n
# Task: Schedule tasks in any order so identical tasks
# are at least n cycles apart, minimizing total CPU cycle time
# Constraints/Complexities: letters only A-Z, n >= 0
# Edge-Cases: n = 0, only one task type, many task types
# Outputs: minimum # of cycles as int

# Non-Optimal/Naive Approach:
# Greedy simulate by cycle, always pick the currently most frequent task not 
# in cooldown
# use a max heap and a cooldown queue
# Time-Complexity: O(T), T ~ len(tasks)
# extra data structures for bookkeeping, slower in practice, cooldown queue
# AND max heap

# Approach:
# count frequencies of 26 letters (A-Z)
# let fmax = # max frequency, k = # of tasks that appear fmax times
# 3 tasks arbitrarily that all have the same FREQUENCY of occuring max times
# place the most frequent tasks first, most often occuring first
# compute the idle math, to determine how long process must wait before being rescheduled
# compute the math, realize no need maxHeap or queue, because we can 
# determine wait length by this formula:
# n = frame length => how many of the most frequently occuring tasks we can place
# first
# idle_time = (fmax - 1) * (n + 1) + k
# answer is the larger of total tasks and idle-based length
# Time-Complexity: O(T), where T ~ len(tasks)
# Space-Complexity: O(1), no extra space

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequency of each uppercase letter
        freq = [0] * 26
        for c in tasks:
            # iterate over all tasks
            # store count of char
            # ASCII value of character using ord
            # A: 48, B: 49, C: 50 50 - 48 => 2
            freq[ord(c) - ord('A')] += 1
        
        # find max frequency among tasks
        fmax = 0
        for c in freq:
            if c > fmax:
                fmax = c

        # count how many task types achieve this maximum frequency
        # this is needed because the last frame may have multiple tasks
        # finishing in the same cycle without extra idles
        # number of tasks with count == fmax
        k = 0
        for c in freq:
            if c == fmax:
                k += 1
        
        # compute idle formula for lower bound using the standard 
        # scheduling formula
        idle_based = (fmax - 1) * (n + 1) + k

        # minimum time is at least number of tasks, since each cycle runs at most
        # one task
        return max(len(tasks), idle_based)
        

