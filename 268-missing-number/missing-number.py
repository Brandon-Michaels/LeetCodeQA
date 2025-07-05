class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach:
        # Time-Complexity: O(nlogn), n is len(nums)
        # Space-Complexity: O(1)
        nums.sort()
        i = -1
        for j in range(len(nums)):
            print(nums[j])
            print(i + 1)
            if (i + 1) != nums[j]:
                return i + 1
            i += 1
        
        return len(nums)