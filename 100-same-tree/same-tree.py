# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Intuition
        # compare root values, then compare left and right values
        # recurse until base-case
        # Time-Complexity: O(nodes in tree)
        # Space-Complexity: Stack size, O(nodes in tree)

        # base-cases
        if (not p and q) or (not q and p):
            return False
        
        if not p and not q:
            return True

        if (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
