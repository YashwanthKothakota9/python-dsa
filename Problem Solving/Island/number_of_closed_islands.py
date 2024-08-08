# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# A closed island is an island that is totally surrounded by 0s (i.e., water). This means all horizontally and vertically connected cells of a closed island are water. This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell).

# Write a function to find the number of closed islands in the given matrix.


# The question follows the Island pattern and is quite similar to Number of Islands problem.

# We will traverse the matrix linearly to find islands. We can use the Depth First Search (DFS) or Breadth First Search (BFS) to traverse an island i.e., to find all of its connected land cells.

# How do we decide if an island is a closed island?

# To find that out, while traversing an island we need to ensure two things:

# The island does not touch an edge.

# Outside boundary of the island are water cells.

# For the first condition, whenever we go outside the boundary of the matrix during DFS or BFS, it means that one of the cells of the island is touching an edge; so, the island is not closed. Following code will cover this condition:

# if (x < 0 || x >= matrix.length || y < 0 || y >= matrix[0].length)
#      return false; // returning false since the island is touching an edge
# For the second condition, we need to ensure that all the boundary cells of the island are water. Following code will take care of that:

# if (matrix[x][y] == 0 || visited[x][y])
#      return true; // returning true as the island is surrounded by water


class Solution:
    def countClosedIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        countClosedIslands = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited[i][j]:
                    if self.is_closed_is_land_DFS(matrix, visited, i, j):
                        countClosedIslands += 1
        
        return countClosedIslands
    
    def is_closed_is_land_DFS(self, matrix, visited, x, y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False # returning false since the island is touching an edge
        if matrix[x][y] == 0 or visited[x][y]:
            return True # returning true as the island is surrounded by water
        
        visited[x][y] = True
        
        isClosed = True
        # recursively visit all neighboring cells (horizontally & vertically)
        isClosed &= self.is_closed_is_land_DFS(matrix, visited, x+1, y)
        isClosed &= self.is_closed_is_land_DFS(matrix, visited, x-1, y)
        isClosed &= self.is_closed_is_land_DFS(matrix, visited, x, y+1)
        isClosed &= self.is_closed_is_land_DFS(matrix, visited, x, y-1)
        
        return isClosed

def main():
  sol = Solution()
  print(sol.countClosedIslands([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [
        0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))

  print(sol.countClosedIslands([[0, 0, 0, 0], [0, 1, 0, 0], [
        0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))


main()
        

# Time Complexity

# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix. This is due to the fact that we have to traverse the whole matrix to find islands.

# Space Complexity

# DFS recursion stack can go M*N deep when the whole matrix is filled with '1's. Hence, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.