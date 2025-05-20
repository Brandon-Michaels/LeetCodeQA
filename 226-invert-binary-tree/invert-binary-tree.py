# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Intuition
        # Invert left and right child recursively up the stack
        # Time-Complexity: O(n), where n is num of nodes in tree
        # Space-Complexity: stack size O(n), recursive approach

        # Base-Case
        if not root:
            return None
            
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        