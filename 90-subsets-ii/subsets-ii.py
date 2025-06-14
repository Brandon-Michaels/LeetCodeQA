class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Approach
        # Same as subsets, recursive dfs to traverse branches of tree
        # find all subsets (or create the power set)
        # to avoid duplicates, sort first, then skip duplicate numbers
        # from being taken
        # Time-Complexity: O(2^n*n), where n len(nums)
        # Space-Complexity: O(2^n), where n len(nums)

        res = []
        nums.sort()

        subsets = []

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return

            subsets.append(nums[i])
            dfs(i + 1)

            # avoid duplicates
            while (i + 1 < len(nums) and nums[i] == nums[i + 1]):
                i += 1
            
            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return res