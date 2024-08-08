# You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.

# A cycle is a path in the matrix that starts and ends at the same cell and has four or more cells. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell.

# Write a function to find if the matrix has a cycle.


# The question follows the Island pattern and is quite similar to Number of Islands problem.

# We will traverse the matrix linearly to find any cycle. Each cycle is like an island having cells containing same values. Hence, we can use the Depth First Search (DFS) or Breadth First Search (BFS) to traverse a cycle i.e., to find all of its connected cells with the same value.

# Our approach for traversing the matrix will be similar to the one we used when searching for islands. We will keep another matrix to remember the cells that we have visited. From any given cell, we can perform DFS to traverse all the neighboring cells having the same character value.

# Whenever we reach a cell that have already been visited, we can conclude that we have found a cycle. This also means that we need to be careful to not start traversing the parent cell and wrongly finding a cycle. That is, while traversing, when initiating DFS recursive calls to all the neighboring cell, we should not start a DFS call to the pervious cell



class Solution:
    def hasCycle(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if self.contains_cycle_DFS(matrix, visited, matrix[i][j], i, j, -1, -1):
                        return True
        
        return False
    
    def contains_cycle_DFS(self, matrix, visited, startChar, x, y, prevX, prevY):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False # not a valid cell
        
        if matrix[x][y] != startChar:
            return False # different character which means a different island
        
        if visited[x][y]:
            return True # found a cycle, as we are visiting an already visited valid cell
        
        visited[x][y] = True # mark the cell visited
        
        if x+1 != prevX and self.contains_cycle_DFS(matrix, visited, startChar, x+1, y, x, y): # down
            return True
        if (x - 1 != prevX and self.contains_cycle_DFS(matrix, visited, startChar, x - 1, y, x, y)): # up
            return True
        if (y + 1 != prevY and self.contains_cycle_DFS(matrix, visited, startChar, x, y + 1, x, y)): # right
            return True
        if (y - 1 != prevY and self.contains_cycle_DFS(matrix, visited, startChar, x, y - 1, x, y)): # left
            return True

        return False


def main():
    sol = Solution()
    print(sol.hasCycle([['a', 'a', 'a', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'a', 'a']]))

    print(sol.hasCycle([['a', 'a', 'a', 'a'],
                    ['a', 'b', 'b', 'a'],
                    ['a', 'b', 'a', 'a'],
                    ['a', 'a', 'a', 'c']]))

    print(sol.hasCycle([['a', 'b', 'e', 'b'],
                    ['b', 'b', 'b', 'b'],
                    ['b', 'c', 'c', 'd'],
                    ['c', 'c', 'd', 'd']]))


main()


# Time Complexity

# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix. This is due to the fact that we have to traverse the whole matrix to find cycles.

# Space Complexity

# DFS recursion stack can go M*N deep when the whole matrix is filled with the same character. Hence, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.