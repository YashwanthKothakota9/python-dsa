# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other.

# Write a function to find the number of distinct islands in the given matrix.


# The question follows the Island pattern and is quite similar to Number of Islands problem.

# We will traverse the matrix linearly to find islands. We can use the Depth First Search (DFS) or Breadth First Search (BFS) to traverse an island i.e., to find all of its connected land cells.

# How do we decide if two islands are same?

# If two islands are same, their traversal path should be same too. This means, if we perform a DFS or BFS on two equal islands starting from their top-left cell, the traversal pattern should be exactly same for both the islands.

# We can utilize this fact to develop an algorithm.

# While traversing an island, we can construct a string that maps the traversal path of the island. For example, here is the DFS traversal of the two same islands mentioned in Example-2 ( 'R' for right move, 'D' for down move, 'O' for origin denoting the start): ORDR

# We can start inserting these traversal strings of each island in a HashSet. This will ensure that we will not have any duplicate traversal string in the HashSet, thus giving us distinct islands. When we finish traversing the matrix, the HashSet will contain the distinct traversal path of all islands. Hence, the total number of elements in the HashSet will be equal to distinct number of islands.


class Solution:
    def findDistinctIslandsDFS(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        islandsSet = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited[i][j]:
                    traversal = self.traverse_is_land_DFS(matrix, visited, i, j, "0")#origin
                    islandsSet.add(traversal)
        
        print(islandsSet)
        return len(islandsSet)
    
    def traverse_is_land_DFS(self, matrix, visited, x, y, direction):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return "" # return if it is not a valid cell
        if matrix[x][y] == 0 or visited[x][y]:
            return "" # return if it is a water cell or is visited
        
        visited[x][y] = True
        
        islandTraversal = direction
        
        islandTraversal += self.traverse_is_land_DFS(matrix, visited, x+1, y, "D")
        islandTraversal += self.traverse_is_land_DFS(matrix, visited, x-1, y, "U")
        islandTraversal += self.traverse_is_land_DFS(matrix, visited, x, y+1, "R")
        islandTraversal += self.traverse_is_land_DFS(matrix, visited, x, y-1, "L")
        
        islandTraversal += "B" # back

        return islandTraversal

def main():
    sol = Solution()
    print(sol.findDistinctIslandsDFS([[1, 1, 0, 1, 1],
                            [1, 1, 0, 1, 1],
                            [0, 0, 0, 0, 0],
                            [0, 1, 1, 0, 1],
                            [0, 1, 1, 0, 1]]))

    print(sol.findDistinctIslandsDFS([[1, 1, 0, 1],
                            [0, 1, 1, 0],
                            [0, 0, 0, 0],
                            [1, 1, 0, 0],
                            [0, 1, 1, 0]]))

main()


# Time Complexity

# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix. This is due to the fact that we have to traverse the whole matrix to find islands.

# Space Complexity

# DFS recursion stack can go M*N deep when the whole matrix is filled with '1's. Hence, the space complexity will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.