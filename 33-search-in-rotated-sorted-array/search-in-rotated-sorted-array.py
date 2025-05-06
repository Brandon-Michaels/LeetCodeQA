class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach
        # check if target is between sorted partition
        # If target not there adjust ptrs or return -1
        # Time-Complexity: O(logn)
        # Space-Complexity: O(1)

        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] <= nums[right]):
                if (target <= nums[right] and target > nums[mid]):
                    left = mid + 1
                else:
                    right = mid - 1
            elif (nums[mid] >= nums[left]):
                if (target >= nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1

        return -1