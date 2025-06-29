class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Approach
        # O's can only be captured if they're not on the edge
        # DFS only on O's from the inside of the grid
        # don't consider any edge O's, DFS on inner O's
        # Think about this in reverse, like Pacific/Atlantic Waterflow
        # traverse from the edges, if any of the edge O's touch inner O
        # then that inner O can't be captured, mark what we can reach as visited
        # recursive DFS from outer edges inwards to find groups of O's reachable
        # from the outside, all O's not reachable capture to X
        # Time-Complexity: O(m * n), where m is len(rows), n is len(cols)
        # Space-Complexity: O(m * n) 

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(i, j, visited):
            if i < 0 or i == rows or j < 0 or j == cols:
                return
            # reached X in DFS, that's fine from an O
            if board[i][j] == "X":
                return
            if ((i, j)) in visited:
                return
            
            visited.add((i, j))

            dfs(i + 1, j, visited)
            dfs(i - 1, j, visited)
            dfs(i, j + 1, visited)
            dfs(i, j - 1, visited)

        # find location of O's on outer edge to start DFS
        for i in range(0, rows):
            if board[i][0] == "O":
                dfs(i, 0, visited)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1, visited)
        
        # find location of O's on outer edge to start DFS
        for j in range(0, cols):
            if board[0][j] == "O":
                dfs(0, j, visited)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j, visited)

        # traverse all of the grid
        # if O not visited then flip to X (not reachable)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"