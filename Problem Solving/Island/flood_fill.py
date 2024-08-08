# Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.

# Given a matrix, a starting cell, and a color, flood fill the matrix.


# The question follows the Island pattern and is quite similar to Number of Islands problem.

# From the given starting cell, we can perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all of its connected cells with the same color. During our DFS or BFS traversal, we will update the cells with the new color.


# Using DFS

class Solution:
    def floodFill(self, matrix, x, y, newColor):
        if matrix[x][y] != newColor:
            self.fill_DFS(matrix, x, y, matrix[x][y], newColor)
        return matrix
    
    def fill_DFS(self, matrix, x, y, oldColor, newColor):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return
        if matrix[x][y] != oldColor:
            return
        
        matrix[x][y] = newColor
        
        self.fill_DFS(matrix, x+1, y, oldColor, newColor)
        self.fill_DFS(matrix, x-1, y, oldColor, newColor)
        self.fill_DFS(matrix, x, y+1, oldColor, newColor)
        self.fill_DFS(matrix, x, y-1, oldColor, newColor)

def main():
  sol = Solution()
  print(sol.floodFill([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], 1, 3, 2))
  print(sol.floodFill([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], 3, 2, 5))


main()

# Time Complexity
# Time complexity the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix. This is due to the fact that, in the worst case, we might have to fill the whole matrix.

# Space Complexity
# DFS recursion stack can go M*N deep when we have to fill the whole matrix. Hence, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.