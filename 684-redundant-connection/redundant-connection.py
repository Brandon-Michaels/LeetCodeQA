class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Approach
        # Recursive DFS on the nodes in the graph
        # if we encounter node we have already seen (excluding going back to the parent)
        # then we know there is a cycle detected, where that cycle occurs, remove that edge
        # Time-Complexity: O(E * (V + E))
        # Space-Complexity: O(V + E)

        nodeToNei = {i:[] for i in range(len(edges) + 1)}

        def dfs(curr, parent):
            if curr in visited:
                return True
            
            visited.add(curr)

            for nei in nodeToNei[curr]:
                if nei == parent:
                    continue
                if dfs(nei, curr):
                    return True

            return False
                
        for curr, nei in edges:
            nodeToNei[curr].append(nei)
            nodeToNei[nei].append(curr)

            visited = set()

            # cycle found if dfs == true
            if dfs(curr, -1):
                return [curr, nei]

        return []
