# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional['TreeNode'], subRoot: Optional['TreeNode']) -> bool:
        if root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s: Optional['TreeNode'], t: Optional['TreeNode']) -> bool:
        if not s and t:
            return False
        if not t and s:
            return False
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        return False