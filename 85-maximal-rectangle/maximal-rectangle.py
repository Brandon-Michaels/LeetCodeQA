class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Handle empty input early so we do not access matrix[0] on an empty matrix.
        if not matrix or not matrix[0]:
            return 0

        # Store matrix dimensions for readability.
        rows = len(matrix)
        cols = len(matrix[0])

        # heights[c] will represent the number of consecutive 1s ending at the
        # current row in column c. This converts each row into a histogram.
        heights = [0] * cols

        # Track the best rectangle area seen across all histogram rows.
        max_area = 0

        # Process each row as the bottom of a histogram.
        for row in range(rows):
            # Update histogram heights:
            # - if current cell is "1", extend the vertical streak
            # - if current cell is "0", reset height to 0 because rectangles
            #   of 1s cannot pass through a 0
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            # Compute the largest rectangle in the current histogram.
            # We use a monotonic increasing stack of indices.
            # The stack stores indices whose heights are in nondecreasing order.
            stack = []

            # We iterate one extra step with a virtual height 0.
            # This forces all remaining bars in the stack to be processed.
            for i in range(cols + 1):
                # The sentinel height 0 at i == cols flushes the stack.
                current_height = 0 if i == cols else heights[i]

                # If the current bar is lower than the bar at the stack top,
                # then the bar at the top can no longer extend to the right.
                # So we pop it and compute the largest rectangle using that
                # popped height as the limiting height.
                while stack and heights[stack[-1]] > current_height:
                    # Height of the rectangle is the popped bar's height.
                    height = heights[stack.pop()]

                    # After popping, the new stack top is the previous smaller bar.
                    # If stack is empty, the rectangle extends all the way to index 0.
                    left_boundary_index = stack[-1] if stack else -1

                    # Width spans from left_boundary_index + 1 through i - 1.
                    width = i - left_boundary_index - 1

                    # Update global best area.
                    area = height * width
                    if area > max_area:
                        max_area = area

                # Push current index so future bars can use it as a boundary.
                stack.append(i)

        # Return the largest rectangle area found in any row histogram.
        return max_area
