class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Approach
        # Recursive DFS traversal over the grid
        # if char match extend dfs
        # else, move in all 4 directions
        # Time-Complexity: O(n * m * 4^len(word)), where m is len(cols), n is len(rows)
        # Space-Complexity: O(n)

        visited = set()

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i >= len(board) or j >= len(board[0]):
                return False
            if i < 0 or j < 0:
                return False
            if board[i][j] != word[index]:
                return False
            if (i, j) in visited:
                return False

            visited.add((i, j))
            # visit all four directions
            res = (dfs(i, j + 1, index + 1) or
            dfs(i + 1, j, index + 1) or
            dfs(i, j - 1, index + 1) or
            dfs(i - 1, j, index + 1))
        
            visited.remove((i,j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (dfs(i, j, 0)):
                    return True
        
        return False