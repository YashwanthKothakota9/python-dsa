# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a function to return the area of the biggest island. 

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).


# The question follows the Island pattern and is quite similar to Number of Islands problem.

# We will traverse the matrix linearly to find islands.

# Whenever we find a cell with the value '1' (i.e., land), we have found an island. Using that cell as the root node, we will perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all of its connected land cells. During our DFS or BFS traversal, we will find and mark all the horizontally and vertically connected land cells. 

# We will keep a variable to remember the max area of any island.


# Using DFS

from typing import List
class Solution:
    def maxAreaOfIsland(self, matrix:List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        biggestIslandArea = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    biggestIslandArea = max(biggestIslandArea, self.visit_is_land_DFS(matrix, i, j))
        
        return biggestIslandArea
    
    def visit_is_land_DFS(self, matrix: List[List[int]], x:int, y:int):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return 0
        if matrix[x][y] == 0:
            return 0
        
        matrix[x][y] = 0
        
        # counting the current cell
        area = 1
        # recursively visit all neighboring cells (horizontally & vertically)
        area += self.visit_is_land_DFS(matrix, x+1, y)
        area += self.visit_is_land_DFS(matrix, x-1, y)
        area += self.visit_is_land_DFS(matrix, x, y+1)
        area += self.visit_is_land_DFS(matrix, x, y-1)
        return area

def main():
  sol = Solution()
  print(sol.maxAreaOfIsland([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))

main()

# Time Complexity
# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix. This is due to the fact that we have to traverse the whole matrix to find islands.

# Space Complexity
# DFS recursion stack can go M*N deep when the whole matrix is filled with '1's. Hence, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.

# 2. Using BFS

from collections import deque

class Solution2:
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.bfs(grid, i, j, directions))
        
        return max_area
    
    def bfs(self, grid, row, col, directions):
        q = deque([(row, col)])
        grid[row][col] = 0
        area = 0
        
        while q:
            current = q.popleft()
            area += 1
            
            for direction in directions:
                new_row, new_col = current[0] + direction[0], current[1] + direction[1]
                
                if 0<=new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = 0
        
        return area


if __name__ == "__main__":
    sol = Solution2()
    print(sol.maxAreaOfIsland([
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]))  # Expected output: 6


# Time Complexity: O(N*M)

# Grid Traversal: The nested for-loops traverse each cell in the grid once. Therefore, this part of the algorithm has a time complexity of O(N*M), where (N) is the number of rows and (M) is the number of columns in the grid.
# BFS Traversal: For each land cell (1), the BFS traversal explores all connected land cells. Since each cell is processed at most once, the total time spent in BFS across all cells is .
# Combining these, the total time complexity is O(N*M).

# Space Complexity:O(N*M)

# Visited Marking: The algorithm marks cells as visited in-place, so no additional space is required for a visited array.
# Queue for BFS: In the worst case, the queue can contain O(min(N,M)) number of cells.
# Therefore, the overall space complexity is O(N*M)+O(min(N,M)), which is equal to O(N*M).