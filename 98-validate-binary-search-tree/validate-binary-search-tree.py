# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Approach:
        # propagate min/max of trees, left is less than, right is greater than
        # Left-subtree, pass down max, right-subtree pass down min
        # Time-Complexity: O(n), n is size nodes in BST
        # Space-Complexity: O(n), size of stack, n is # nodes in BST

        def dfs(curr, minVal, maxVal):
            if not curr:
                return True
            
            if ((curr.val) >= maxVal or (curr.val) <= minVal):
                return False
            
            return (dfs(curr.left, minVal, curr.val) 
            and dfs(curr.right, curr.val, maxVal))
        
        return dfs(root, float("-inf"), float("inf"))