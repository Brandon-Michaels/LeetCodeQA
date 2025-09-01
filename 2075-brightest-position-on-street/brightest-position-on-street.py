# Problem Summary
# Input: 2D integer array lights, lights[i] = [position, range] street light
# Task: Find and return brightest position on the street, if tie return smallest position
# brightest position is defined as the # of street lamps that light up a position
# overlapping intervals count, so if [-1, 1], [1,3], 1 is illuminated by 2 lights
# Complexities/Constraints: lights => int array
# Edge-Cases: no lights, no overlapping intervals => return smallest lit position
# Output: return the brightest position on the street (int)

# Non-Optimal / Naive Approach:
# Create new 2D array which intervals of fully illuminated positions
# [-3, 2] => [-5, -1], count overlaps in HashMap
# Brute Force Traverse through that array and count overlapping intervals
# max overlapping interval will be the position we return from
# smallest position in that interval we return from

# Approach
# Sweep Line => Prefix Sum
# Traverse brightest position in sorted order
# Sort input lights list => O(nlogn), n is len(lights)
# Track max and smallest position, use two variables O(1)
# Difference map on integer endpoints => 'diff'
# For left edge, diff[L] += 1, for one past right edge, diff[R + 1] -= 1
# we subtract by one to cancel out the adding on left edge
# if you only added, we would just get that the last street lamp district is most covered
# subtracting by one cancels out the coverage
# Time-Complexity: O(nlogn) for sorting, n ~ len(lights)
# Space-Complexity: O(n), n ~ len(lights)

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # difference map, position => brightness
        diff = {}

        # traverse lights
        # get L,R boundaries for each element
        for pos, rng in lights:
            L = pos - rng
            R = pos + rng
            diff[L] = diff.get(L, 0) + 1
            diff[R + 1] = diff.get(R + 1, 0) - 1

        # traverse diff, determine max illumination
        # initialize variables to track brightness
        max_brightness = float('-inf')
        min_position = 0
        
        # current brightness at position
        running = 0

        # sort unique breakpoints
        for x in sorted(diff.keys()):
            # update brightness at x
            running += diff[x]
            if running > max_brightness:
                max_brightness = running
                # update min position to curr, processed in order
                min_position = x

        return min_position



        









