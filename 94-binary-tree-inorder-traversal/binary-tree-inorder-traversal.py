# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # The stack holds ancestors waiting to be visited after their left subtrees
        stack = []
        # The result stores values in left-node-right order.
        result = []
        current = root

        while current is not None or stack:
            # Defer each node until its entire left subtree has been visited.
            while current is not None:
                stack.append(current)
                current = current.left

            # The left subtree is complete, so record this node next.
            current = stack.pop()
            result.append(current.val)

            # Visit the right subtree before returning to a waiting ancestor.
            current = current.right

        return result

        