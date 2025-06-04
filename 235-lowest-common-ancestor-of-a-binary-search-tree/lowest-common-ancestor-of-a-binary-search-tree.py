# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Approach:
        # Since BST, if both p and q are apart of different subtrees (i.e. their
        # values split the problem into 2 subtrees)
        # then the LCA is the curr node, else iterate on left/right respectively
        # Dividing space into halves
        # Time-Complexity: O(logn), n is the # nodes in the BST
        # Space-Complexity: O(1), no external storage needed

        curr = root

        while curr:
            if (p.val < curr.val and q .val < curr.val):
                curr = curr.left
            elif (p.val > curr.val and q .val > curr.val):
                curr = curr.right
            else:
                return curr
