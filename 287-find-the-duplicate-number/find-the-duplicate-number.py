class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time-Complexity: O(n)
        # Space-Complexity: O(n), where n is size of list nums
        # numSet = set()

        # for n in nums:
        #     if (n in numSet):
        #         return n
        #     numSet.add(n)

        # Alternative Approach:
        # Sort -> Time-Complexity: O(nlogn)
        # Space-Complexity: O(1)

        # Optimized:
        # Intuition:
        # Negate values as you traverse them, 1 -> -1, 2 -> -2
        # if you go back to original index where it is encountered, 
        # abs(nums[i]) - 1, you can see at that spot if it is neg. if
        # so, then return that number
        # Time-Complexity: O(n)
        # Space-Compleixty: O(1)

        for i in range(0, len(nums)):
            # if curr. position alr. negative => seen alr. return num.
            if (nums[abs(nums[i]) - 1] < 0):
                return abs(nums[i])
            # negates curr. position
            nums[abs(nums[i]) - 1] *= -1

        