# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).


# Solution

# We can traverse the matrix linearly to find islands.

# Whenever we find a cell with the value '1' (i.e., land), we have found an island. Using that cell as the root node, we will perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all of its connected land cells. During our DFS or BFS traversal, we will find and mark all the horizontally and vertically connected land cells. 

# We need to have a mechanism to mark each land cell to ensure that each land cell is visited only once. To mark a cell visited, we have two options:

# We can update the given input matrix. Whenever we see a '1', we will make it '0'.
# A separate boolean matrix can be used to record whether or not each cell has been visited. 


# 1. DFS

from typing import List

class Solution:
    def countIslands(self, matrix:List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    totalIslands += 1
                    self.visit_is_land_DFS(matrix, i, j)
        
        return totalIslands

    def visit_is_land_DFS(self, matrix: List[List[int]], x:int, y:int):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return # return, if it is not a valid cell
        if matrix[x][y] == 0:
            return # return, if it is a water cell
        
        matrix[x][y] = 0
        
        # recursively visit all neighboring cells (horizontally & vertically)
        self.visit_is_land_DFS(matrix, x+1, y) # lower cell
        self.visit_is_land_DFS(matrix, x-1, y) # upper cell
        self.visit_is_land_DFS(matrix, x, y+1) # right cell
        self.visit_is_land_DFS(matrix, x, y-1) # left cell


def main():
  sol = Solution()
  print(sol.countIslands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))
  print(sol.countIslands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))



main()


# Time Complexity
# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix. This is due to the fact that we have to traverse the whole matrix to find the islands.

# Space Complexity
# DFS recursion stack can go M*N deep when the whole matrix is filled with '1's. Hence, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.


# 2. BFS

from collections import deque

class Solution2:
    def countIslands(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    totalIslands += 1
                    self.visit_is_land_BFS(matrix, i, j)
        
        return totalIslands

    def visit_is_land_BFS(self, matrix: List[List[int]], x: int, y: int):
        neighbors = deque([(x, y)])
        while neighbors:
            row, col = neighbors.popleft()
            
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue
            if matrix[row][col] == 0:
                continue
            
            matrix[row][col] = 0
            
            neighbors.extend([(row+1, col)])
            neighbors.extend([(row-1, col)])
            neighbors.extend([(row, col+1)])
            neighbors.extend([(row, col-1)])


def main2():
    sol = Solution2()
    print(sol.countIslands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], 
                            [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))
    print(sol.countIslands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], 
                            [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))

main2()


# Time Complexity
# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns.

# Space Complexity
# Space complexity of the above algorithm will be O(min(M,N)). In the worst case, when the matrix is completely filled with land cells, the size of the queue can grow up to min(M,N).


# 3. BFS with visited matrix

class Solution3:
    def countIslands(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0
        visited = [[False for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited[i][j]:
                    totalIslands += 1
                    self.visit_is_land_BFS(matrix, visited, i, j)
        
        return totalIslands
    
    def visit_is_land_BFS(self, matrix: List[List[int]], visited ,x:int, y:int):
        neighbors = deque([(x, y)])
        while neighbors:
            row, col = neighbors.popleft()
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue
            if matrix[row][col] == 0 or visited[row][col]:
                continue
            
            visited[row][col] = True
            
            neighbors.extend([(row + 1, col)])
            neighbors.extend([(row - 1, col)])
            neighbors.extend([(row, col + 1)])
            neighbors.extend([(row, col - 1)])
            

def main3():
  sol = Solution()
  print(sol.countIslands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))
  print(sol.countIslands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))



main3()


# Time Complexity
# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns.

# Space Complexity
# Because of the visited array and max size of the queue, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.