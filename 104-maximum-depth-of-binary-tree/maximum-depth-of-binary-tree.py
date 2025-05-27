# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Intuition:
        # recursively call maxDepth on left/right sub-tree
        # increment depth by one each time
        # Time-Complexity: O(nodes in tree)
        # Space-Complexity: size of stack, O(h), where h is height of tree
        # worst-case degenerate, otherwise O(log nodes)

        if not root:
            return 0
        
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)