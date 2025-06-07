# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Approach:
        # Propagate max node value through dfs levels
        # If node is >= max, then increment counter, else don't
        # Time-Complexity: O(n), where n is size of tree
        # Space-Complexity: O(n), where n is size of tree, for size of stack

        res = 0

        def dfs(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            
            return res

        return dfs(root, root.val)

