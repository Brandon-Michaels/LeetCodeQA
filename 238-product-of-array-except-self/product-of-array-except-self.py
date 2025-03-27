class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach: Prefix / Suffix
        # O(n) Time-Complexity, where n is the length of nums
        # O(n) Space-Complexity, where n is the length of nums
        # calculate each indices prefix and suffix products
        # store these in an array, then multiply prefix and suffix to 
        # compute product of array except self

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prefix[0] = suffix[len(nums) - 1] = 1

        # iterate left to right to get product of prefix array
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # iterate from right to left to get product of suffix array
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Calculate output by multiplying prefix and suffix arrays
        output = [0] * len(nums)
        for i in range(0, len(nums)):
            output[i] = prefix[i] * suffix[i]
        
        return output