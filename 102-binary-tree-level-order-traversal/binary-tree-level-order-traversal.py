# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach
        # Use BFS with queue, to add next nodes to queue
        # repeat until queue is empty, each new depth create new list
        # Time-Complexity: O(n), where n is number of nodes
        # Space-Complexity: O(n), where n is number of nodes, size of stack

        queue = []
        queue.append(root)
        res = []

        while (queue):
            qLen = len(queue)
            level = []
            for i in range(0, qLen):
                curr = queue.pop(0)
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                res.append(level)
        
        return res