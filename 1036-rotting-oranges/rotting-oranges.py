class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Approach
        # very similar to walls and gates
        # Do a BFS from all the rotten fruits, if you encounter
        # vertically or horizontally a fresh fruit, then make that
        # square also rotten, repeat until no more squares reachable
        # Time-Complexity: O(m * n), where m is len(rows), n is len(cols)
        # Space-Complexity: O(m * n), where m is len(rows), n is len(cols)


        rows = len(grid)
        cols = len(grid[0])
        frontier = deque()
        dist = 0
        freshCount = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # traverse grid for rotten fruit
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    frontier.append((i, j))
                if grid[i][j] == 1:
                    freshCount += 1
        
        # bfs
        while freshCount > 0 and frontier:
            for node in range(len(frontier)):
                r, c = frontier.popleft()
                # traverse all 4 directions
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols)
                    and grid[row][col] == 1):
                        freshCount -= 1
                        grid[row][col] = 2
                        frontier.append((row, col))
            
            dist += 1
            
        if freshCount == 0:
            return dist
        else:
            return -1


