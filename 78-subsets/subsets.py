class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Approach:
        # Traverse decision tree, use recursive dfs approach
        # decide whether to include or not include current element
        # Time-Complexity: O(n * 2^n), n is len(nums)
        # Space-Complexity: O(2^n), n is len(nums)

        res = []

        subset = []

        # i == current index we are at in nums
        def dfs(i):
            # base-case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # add element
            subset.append(nums[i])
            dfs(i + 1)

            # ignore element / don't take element
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res