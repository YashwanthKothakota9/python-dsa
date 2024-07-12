# Imagine a country with several cities. Some cities have direct roads connecting them, while others might be connected through a sequence of intermediary cities. Using a matrix representation, if matrix[i][j] holds the value 1, it indicates that city i is directly linked to city j and vice versa. If it holds 0, then there's no direct link between them.

# Determine the number of separate city clusters (or provinces).

# A province is defined as a collection of cities that can be reached from each other either directly or through other cities in the same province.

# Input:
# [[1,1,0],[1,1,0],[0,0,1]]
# Expected Output:
# 2
# Justification:
# There are two provinces: cities 0 and 1 form one province, and city 2 forms its own province.
# Input:
# [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]
# Expected Output:
# 2
# Justification:
# There are two provinces: cities 0 and 3 are interconnected forming one province, and cities 1 and 2 form another.
# Input:
# [[1,0,0],[0,1,0],[0,0,1]]
# Expected Output:
# 3
# Justification:
# Each city stands alone and is not connected to any other city. Thus, we have three provinces.


# At a high level, the problem of identifying provinces in the given matrix can be visualized as detecting connected components in an undirected graph. Every city represents a node, and a direct connection between two cities is an edge. The number of separate, interconnected clusters in this graph is essentially the number of provinces. To navigate this graph and identify these clusters, we employ the Depth First Search (DFS) technique, marking visited nodes (cities) along the way.

# Initialization: Start with a visited array, initialized with all values set to false. This will help in keeping track of cities that have been processed.
# DFS Function: This recursive function allows us to traverse the matrix. When an unvisited city is found, we recursively visit all other cities accessible from it, marking them as visited. All cities traversed in a single DFS invocation belong to the same province.
# Counting Provinces: Every unique invocation of the DFS function on an unvisited city, from the main function, signifies the discovery of a new province. Therefore, for each such invocation, we increment our province count.
# Completion: After every city has been visited, our province counter will hold the total number of provinces in the country.

class Solution:
    def findCircleNum(self, isConnected) -> int:
        
        def dfs(city):
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)
        
        visited = [False] * len(isConnected)
        provinces = 0
        
        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(city)
                province += 1
        
        return provinces
    
solution = Solution()
print(solution.findCircleNum([[1,1,0], [1,1,0], [0,0,1]]))  # Expected output: 2
print(solution.findCircleNum([[1,0,0,1], [0,1,1,0], [0,1,1,0], [1,0,0,1]]))  # Expected output: 2
print(solution.findCircleNum([[1,0,0], [0,1,0], [0,0,1]]))  # Expected output: 3

# Time Complexity: (O(n^2))
# Space Complexity: (O(n))