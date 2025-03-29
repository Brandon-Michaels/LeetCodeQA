class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach: Run binary search on target
        # Time-Complexity: O(logn)
        # Space-Complexity: O(1)

        left = 0
        right = len(nums) - 1

        while (left <= right):
            middle = (left + right) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle - 1
            else:
                left = middle + 1
        
        return -1