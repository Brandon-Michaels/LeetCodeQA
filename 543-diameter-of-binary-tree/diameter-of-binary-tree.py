# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time-Complexity: O(nodes in tree)
        # Space-Complexity: Size of stack, O(height), worst-case degenerate O(nodes in tree)

        sol = 0

        def dfs(root):
            nonlocal sol

            # base-case
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            sol = max(left + right, sol)

            return 1 + max(left, right)
        
        dfs(root)
        return sol