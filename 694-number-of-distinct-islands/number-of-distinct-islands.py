class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        unique_shapes = set()
        visited = set()

        def dfs(r, c, r0, c0, current_shape):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited):
                return
            
            visited.add((r, c))
            current_shape.append((r - r0, c - c0))

            dfs(r + 1, c, r0, c0, current_shape)
            dfs(r - 1, c, r0, c0, current_shape)
            dfs(r, c + 1, r0, c0, current_shape)
            dfs(r, c - 1, r0, c0, current_shape)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_shape = []
                    dfs(r, c, r, c, current_shape)
                    unique_shapes.add(tuple(current_shape))

        return len(unique_shapes)