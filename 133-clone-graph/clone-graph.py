"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Approach
        # BFS on the graph, add curr node mapping to create 1:1 mapping between
        # old and new nodes
        # While frontier is not empty, visit neighbors
        # add neighbors to map to ensure we keep track of cloned nodes, repeat
        # deep copy means new memory location, not references to the old pointers
        # visited set is NOT enough, bc that prevents cycles but doesn't create deep copy
        # to create deep copy you need to have mapping so before you create new node, you know if it's
        # been cloned already 
        # deque, append right, pop left
        # Time-Complexity: O(V + E), where V is # of vertices, E # of edges
        # Space-Complexity: O(E), frontier is max # edges connected to any node

        oldToNew = {}
        frontier = deque()

        if not node:
            return None

        # creates new to old node mapping
        oldToNew[node] = Node(node.val)
        frontier.append(node)

        while (frontier):
            curr = frontier.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    # then we haven't cloned 
                    oldToNew[neighbor] = Node(neighbor.val)
                    frontier.append(neighbor)

                oldToNew[curr].neighbors.append(oldToNew[neighbor])
        
        return oldToNew[node]