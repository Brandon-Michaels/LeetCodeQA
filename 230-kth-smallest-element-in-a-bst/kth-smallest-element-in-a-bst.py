# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach:
        # in-order traversal, smallest => largest, return kth node in an
        # in-order traversal
        # Time-Complexity: O(n), where n is # nodes in BST
        # Space-Complexity: O(n), where n is # nodes in BST, size of stack

        res = []
        def dfs(curr):
            # left, curr, right
            if not curr:
                return
            
            dfs(curr.left)
            res.append(curr.val)
            dfs(curr.right)
        
        dfs(root)
        return res[k - 1]