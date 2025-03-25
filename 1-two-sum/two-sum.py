class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach:
        # Time-Complexity: O(n), n is length of nums list
        # Space-Complexity: O(n), worst-case all nums added to dictionary
        # Dict: key: nums[i], value: index of nums[i]

        prev_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in prev_dict:
                return [prev_dict[target - nums[i]], i]
            prev_dict[nums[i]] = i