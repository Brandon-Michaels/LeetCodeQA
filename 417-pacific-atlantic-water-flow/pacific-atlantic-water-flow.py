class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Naive Approach
        # Recursive DFS on all cells
        # Only if it can reach (top or left) and (bottom or right)
        # add (r, c) to 2D array
        # bottom/left, top/right corners always valid
        # Time-Complexity: O(m^2 * n^2)
        # Space-Complexity: O(m^2 * n^2)

        # Optimized Approach
        # Recursive DFS only on cells bordering one of the Oceans
        # keep visited hash set so we don't run dfs again on cells
        # that we already have seen/know the result to
        # Only if it can reach (top or left) and (bottom or right)
        # add (r, c) to 2D array
        # bottom/left, top/right corners always valid
        # Time-Complexity: O(m * n)
        # Space-Complexity: O(m * n)

        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def dfs(r, c, prevHeight, visited):
            if (r < 0 or c < 0 or r == rows or c == cols):
                return
            if ((r, c) in visited):
                return
            if heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))
            # visit all 4 directions
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)

        for i in range(rows):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, cols - 1, heights[i][cols - 1], atlantic)
        
        for j in range(cols):
            dfs(0, j, heights[0][j], pacific)
            dfs(rows - 1, j, heights[rows - 1][j], atlantic)

        # traverse grid, see if in both sets
        for r in range(rows):
            for c in range(cols):
                if ((r, c) in atlantic and (r, c) in pacific):
                    res.append([r, c])
        
        return res