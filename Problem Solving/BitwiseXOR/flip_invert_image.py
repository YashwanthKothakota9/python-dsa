# Given a square binary matrix representing an image, we want to flip the image horizontally, then invert it.

# To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

# Example 1:

# Input: [
#   [1,0,1],
#   [1,1,1],
#   [0,1,1]
# ]
# Output: [
#   [0,1,0],
#   [0,0,0],
#   [0,0,1]
# ]
# Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

# Example 2:

# Input: [
#   [1,1,0,0],
#   [1,0,0,1],
#   [0,1,1,1], 
#   [1,0,1,0]
# ]
# Output: [
#   [1,1,0,0],
#   [0,1,1,0],
#   [0,0,0,1],
#   [1,0,1,0]
# ]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


# Flip: We can flip the image in place by replacing ith element from left with the ith element from the right.
# Invert: We can take XOR of each element with 1. If it is 1 then it will become 0 and if it is 0 then it will become 1.


class Solution:
  def flipAndInvertImage(self, matrix):
    C = len(matrix[0])  # Get the number of columns in the matrix
    for row in matrix:
      for i in range((C+1)//2):  # Iterate through the first half of the row
        # Swap and invert elements symmetrically from the beginning and end of the row
        row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
        
    return matrix

def main():
  sol = Solution()
  print(sol.flipAndInvertImage([[1,0,1], [1,1,1], [0,1,1]]))
  print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()

# Time Complexity
# Outer Loop:

# The outer loop iterates over each row of the matrix. If the matrix has ( N ) rows, this loop runs ( N ) times.
# Inner Loop:

# For each row, the inner loop runs for half of the columns (or one more than half if the number of columns is odd). If there are ( N ) columns, the inner loop runs N/2 times.
# Each iteration of the inner loop performs constant-time operations (XOR and assignments), the total time complexity is: O(N*N) where ( N ) is the number of rows and the number of columns.

# Space Complexity
# In-place Modification:

# The flipAndInvertImage function modifies the matrix in place, so no additional space is required for creating a new matrix.
# Auxiliary Space:

# The only additional space used is for the temporary variable tmp inside the inner loop. This requires O(1) space.
# Therefore, the space complexity of the function is: O(1)