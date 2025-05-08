class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two-Pointer Approach
        # Intuition, input array is sorted
        # Move left ptr if sum of left + right is too small
        # Move right ptr if sum of left + right is too large
        # Time-Complexity: O(n), n is the size of numbers array
        # Space-Complexity: O(1)

        left = 0
        right = len(numbers) - 1

        while (left < right):
            if (numbers[left] + numbers[right] == target):
                return list((left + 1, right + 1))
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                right -= 1

        return 0