class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Divide and Conquer
        # Start with middle element in row, since we know each row is non-decreasing
        # i.e. sorted, then we can check (left, right, up, down) O(1)
        # Binary search on columns
        # Binary search on middle row

        bottom_row = 0
        top_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1

        while (bottom_row <= top_row):
            middle_row = (bottom_row + top_row) // 2
            if (target > matrix[middle_row][-1]):
                bottom_row = middle_row + 1
            elif (target < matrix[middle_row][0]):
                top_row = middle_row - 1
            else:
                break
        
        if (bottom_row > top_row):
            return False
            
        while (left_col <= right_col):
            middle_col = (left_col + right_col) // 2
            if (matrix[middle_row][middle_col] == target):
                return True
            elif (matrix[middle_row][middle_col] > target):
                right_col = middle_col - 1
            else:
                left_col = middle_col + 1

        return False