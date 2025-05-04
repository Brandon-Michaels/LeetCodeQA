class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Divide and Conquer Approach
        # Compare middle element to left/right ptr
        # if middle smallest, return
        # else, search left/right respectively
        # Time-Complexity: O(logn)
        # Space-Complexity: O(1)
    
        leftPtr = 0
        rightPtr = len(nums) - 1

        while (leftPtr < rightPtr):
            middleIdx = (leftPtr + rightPtr) // 2
            if (nums[middleIdx] > nums[rightPtr]):
                leftPtr = middleIdx + 1
            else:
                rightPtr = middleIdx
        
        return min(nums[leftPtr], nums[rightPtr])