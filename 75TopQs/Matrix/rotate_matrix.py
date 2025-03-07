# Given an n x n 2D matrix, modify a square matrix by rotating it 90 degrees in a clockwise direction.

# Note: This rotation should be done in-place, meaning the transformation must occur within the original matrix without using any additional space for another matrix.

# Examples
# Example 1:
# Input: matrix =
# [[1,2],
#  [3,4]]
# Expected Output:
# [[3,1],
#  [4,2]]

# Solution
# To solve this problem, we'll employ a two-step approach: first, transpose the matrix, and then reverse each row. Transposing the matrix swaps the row and column indices for each element, effectively rotating the matrix by 90 degrees but in the wrong direction. Reversing each row afterward aligns the matrix correctly for the desired 90-degree rotation to the right.

# This method is effective because it directly manipulates the matrix in place, adhering to the in-place requirement, and it systematically rearranges the elements to achieve the rotation without needing additional storage.

# Step-by-step Algorithm
# Transpose the Matrix:

# Iterate over the matrix with two nested loops, where the outer loop variable i runs from 0 to n-1 (inclusive) and the inner loop variable j runs from i to n-1 (inclusive).
# For each pair (i, j), swap the elements at positions [i][j] and [j][i]. This effectively changes rows into columns, transposing the matrix.
# Reverse Each Row:

# After the matrix is transposed, iterate over each row of the matrix with a single loop where the loop variable i runs from 0 to n-1 (inclusive).
# For each row i, reverse the elements in the row. To do this, use a second loop where you swap elements from the start and end of the row moving towards the center. The loop variable j runs from 0 to (n/2)-1 (inclusive), and for each iteration, swap the elements at positions [i][j] and [i][n-1-j].

# Time Complexity
# O(n^2): The algorithm iterates over each element of the matrix twice. First, during the transposition step, each element is visited once. Second, when reversing the rows, each element is again accessed once. Since the matrix is of size n x n, the total time complexity is .
# Space Complexity
# O(1): The rotation is performed in-place, which means no additional storage is required beyond temporary variables that are used for swapping elements. This results in a constant space complexity.


class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
        return matrix


if __name__ == "__main__":
    solution = Solution()
    matrix = [[10, 11, 12, 13], [14, 15, 16, 17],
              [18, 19, 20, 21], [22, 23, 24, 25]]
    solution.rotate(matrix)
    print("Rotated Matrix:", matrix)
