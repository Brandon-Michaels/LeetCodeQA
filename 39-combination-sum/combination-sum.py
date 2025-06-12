class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Approach:
        # Use recursive DFS to traverse the combination sum decision tree
        # To prevent duplicate arr: include curr num, then exclude num
        # for future distinct branches of the tree
        # Time-Complexity: O(2^t), where t is the target number
        # Space-Complexity: O(t), where t is the target number

        res = []

        def dfs(i, currArr, total):
            if (total == target):
                res.append(currArr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # take curr element and prevent it from being used
            # in distinct new branches of the tree
            currArr.append(nums[i])
            dfs(i, currArr, total + nums[i])

            currArr.pop()
            dfs(i + 1, currArr, total)

        dfs(0, [], 0)
        return res