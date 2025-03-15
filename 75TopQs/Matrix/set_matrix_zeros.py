# Given a 2D grid of numbers called matrix, if any number in the grid is 0, set the entire row and column containing that zero to zeros.

# The grid should be modified in place without using any extra grid.

# Examples
# Example 1:

# Input: matrix =
# [[2, 3, 4],
#  [5, 0, 6],
#  [7, 8, 9]]
# Expected Output:
# [[2, 0, 4],
#  [0, 0, 0],
#  [7, 0, 9]]
# Justification: The element at position(1, 1) is zero. So, the second row and column are set to zero.
# Example 2:

# Input: matrix =
# [[0, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Expected Output:
# [[0, 0, 0],
#  [0, 5, 6],
#  [0, 8, 9]]
# Justification: The element at position(0, 0) is zero. So, the first row and column are set to zero.
# Example 3:

# Input: matrix =
# [[1, 2, 3, 7],
#  [4, 0, 6, 8],
#  [0, 8, 9, 6],
#  [1, 4, 6, 4]]
# Expected Output:
# [[0, 0, 3, 7],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 6, 4]
# Justification: The elements at position(1, 1), and (2, 0) are zero. So, the respected rows and columns are set to zero.

# Solution
# To solve this problem, we use the first row and first column of the matrix to mark the rows and columns that need to be set to zero. This way, we can avoid using extra space for marking. Initially, we traverse the matrix to find the cells that contain zeros. If a cell at position(i, j) is zero, we set the first cell of the i-th row and the first cell of the j-th column to zero. We also use a boolean variable to track if the first column itself needs to be zeroed.

# This approach works because we are only modifying the first row and first column during the first pass . In the second pass, we use these markers to set the appropriate cells to zero. Finally, we handle the first row and first column separately to ensure the markers themselves do not interfere with the zeroing process. This method ensures the solution is both space-efficient and straightforward.

# Step-by-Step Algorithm
# Initialize: Create a boolean variable isCol and set it to false. This will track if the first column needs to be zeroed.
# First Pass:
# Loop through each element of the matrix.
# If any element in the first column is zero, set isCol to true.
# For each zero element in the matrix(not in the first column), set the first element of its row and column to zero.
# Second Pass:
# Loop through the matrix starting from the second row and second column.
# If the first element of the row or column is zero, set the corresponding element to zero.
# Handle First Row:
# If the first element of the first row is zero, set all elements in the first row to zero.
# Handle First Column:
# If isCol is true, set all elements in the first column to zero.
# Return the matrix.

# Complexity Analysis
# Time Complexity
# The time complexity of the solution is O(M*N), where M is the number of rows and N is the number of columns in the matrix. This is because we traverse the matrix twice: once for marking and once for setting zeroes.

# Space Complexity
# The space complexity of the solution is O(1), as we are not using any extra space that scales with the input size.


class Solution:
    def set_zeros(self, matrix):
        is_col = False
        R = len(matrix)
        C = len(matrix[0])

        # First Pass
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Second pass
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

        return matrix


if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[2, 3, 4], [5, 0, 6], [7, 8, 9]]
    print(solution.set_zeros(matrix1))
    # Expected: [[2, 0, 4], [0, 0, 0], [7, 0, 9]]

    matrix2 = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.set_zeros(matrix2))
    # Expected: [[0, 0, 0], [0, 5, 6], [0, 8, 9]]

    matrix3 = [[1, 2, 3, 7], [4, 0, 6, 8], [0, 8, 9, 6], [1, 4, 6, 4]]
    print(solution.set_zeros(matrix3))
    # Expected: [[0, 0, 3, 7], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 6, 4]]
