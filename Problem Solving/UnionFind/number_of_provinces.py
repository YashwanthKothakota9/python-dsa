# There are n cities. Some of them are connected in a network. If City A is directly connected to City B, and City B is directly connected to City C, city A is directly connected to City C.

# If a group of cities are connected directly or indirectly, they form a province.

# Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise, determine the total number of provinces.

# Examples
# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Expected Output: 2

# Justification: Here, city 1 and 2 form a single provenance, and city 3 is one provenance itself.

# Example 2:

# Input: isConnected = [1,0,0],[0,1,0],[0,0,1]]
# Expected Output: 3

# Justification: In this scenario, no cities are connected to each other, so each city forms its own province.

# Example 3:

# Input: isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]
# Expected Output: 2
# Justification: Cities 1 and 4 form a province, and cities 2 and 3 form another province, resulting in a total of 2 provinces.

# To solve this problem, we'll employ the Union-Find algorithm, a powerful algorithm for managing disjoint sets. The essence of the approach is to group cities into sets, where each set represents a connected province.

# Initially, every city is considered its own province. As we go through the matrix, we use Union operations to join cities that are directly connected, effectively merging their sets. The Find operation identifies the representative of each set (or province) and helps in determining if two cities are already in the same province. By iteratively applying Union operations to all connected city pairs, we merge their respective sets.

# In the end, the number of distinct sets (or provinces) is determined by counting the unique representatives of each set, providing the solution to our problem. This approach ensures efficient handling of connections and an accurate count of disconnected provinces.


# Step-by-Step Algorithm
# Initialization:

# Create a Union-Find data structure with parent and rank arrays.
# Initialize the parent array such that each node is its own parent.
# Initialize the rank array with zeros.
# Process the Connections:

# For each pair of nodes (i, j) in the adjacency matrix isConnected:
# If isConnected[i][j] is 1, indicating a direct connection:
# Use the find operation to check the roots of nodes i and j.
# If the roots are different, decrement the numberOfProvinces and perform the union operation to merge the sets containing nodes i and j.
# Return the Result:

# The final value of numberOfProvinces represents the number of connected components or provinces.

# Algorithm Walkthrough
# Given an input isConnected = [[1,1,0],[1,1,0],[0,0,1]], let's walk through the algorithm:

# Initial Setup
# Initialization:

# parent = [0, 1, 2] (each node is its own parent)
# rank = [0, 0, 0] (initial ranks are zero)
# numberOfProvinces = 3 (initially, each node is its own province)
# First Node (i = 0):

# (i = 0, j = 1):
# isConnected[0][1] = 1 (nodes 0 and 1 are connected)
# find(0) returns 0 (root of 0)
# find(1) returns 1 (root of 1)
# Roots are different, so decrement numberOfProvinces to 2.
# Perform union_set(0, 1):
# find(0) returns 0
# find(1) returns 1
# rank[0] == rank[1], so attach root of 1 to root of 0 and increment rank[0].
# Updated parent = [0, 0, 2] and rank = [1, 0, 0].
# Second Node (i = 1):
# (i = 1, j = 2):
# isConnected[1][2] = 0 (nodes 1 and 2 are not connected)
# No action needed.
# Third Node (i = 2):
# No connections to check (as j only goes from i+1 to n).
# The final count of provinces is 2.

class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.rank = [0]*size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union_set(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # If they are in the same set, do nothing.
        if rootX == rootY:
            return

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


class Solution:
    def findProvinces(self, isConnected):
        n = len(isConnected)
        uf = UnionFind(n)
        numberOfProvinces = n

        # Iterate over each pair of nodes and union the sets if there is a connection.
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    numberOfProvinces -= 1
                    uf.union_set(i, j)

        return numberOfProvinces


# Main method for testing
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    example1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example1))  # Expected Output: 2

    # Example 2
    example2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example2))  # Expected Output: 3

    # Example 3
    example3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    print(solution.findProvinces(example3))  # Expected Output: 2


# Time Complexity
# Initialization:

# Initializing the parent and rank arrays takes O(N) time, where (N) is the number of nodes (or cities).
# Find Operation:

# The find operation with path compression has an amortized time complexity of O(alpha(N)), where is alpha(N) the inverse Ackermann function. This function is extremely slow-growing and can be considered nearly constant for practical input sizes.
# Union Operation:

# The union_set operation involves two find operations and one assignment, leading to a time complexity of O(alpha(N)) per union.
# Processing Connections:

# The nested loops iterate through each pair of nodes to check for connections. This involves O(N ^ 2) iterations, where each iteration involves at most two find operations and one union_set operation. Thus, the total time complexity for processing all connections is O(N ^ 2*alpha(N)).
# Given that alpha(N) is nearly constant, the overall time complexity can be simplified to O(N ^ 2).

# Space Complexity
# Parent and Rank Arrays:
# The parent and rank arrays require O(N) space each, where(N) is the number of nodes.


# Alternate Approach (Using DFS)
# At a high level, the problem of identifying provinces in the given matrix can be visualized as detecting connected components in an undirected graph. Every city represents a node, and a direct connection between two cities is an edge. The number of separate, interconnected clusters in this graph is essentially the number of provinces. To navigate this graph and identify these clusters, we employ the Depth First Search (DFS) technique, marking visited nodes (cities) along the way.

# Step-by-step Algorithm
# Initialization:

# Initialize an integer variable provinces to 0. This will count the number of distinct provinces.
# Create a visited array of the same size as the number of cities (isConnected.size()), initialized to false. This array keeps track of whether a city has been visited.
# Iterate Over Each City:

# Loop through each city i from 0 to n-1 (where n is the number of cities).
# For each city i, check if it has been visited. If not, it indicates the start of a new province.
# Increment the provinces counter, as this city marks the start of a new province.
# Call the dfs method to explore all cities connected to city i.
# Depth-First Search (DFS):

# In the dfs method, start with city i.
# Loop through each city j from 0 to n-1.
# If city i is connected to city j (isConnected[i][j] == 1) and city j has not been visited (!visited[j]), mark city j as visited (visited[j] = true).
# Recursively call the dfs method with city j as the new starting point to explore all its connected cities.
# Repeat DFS for Each Province:

# Once the DFS completes for a city, return to the main loop in the findCircleNum method and continue with the next unvisited city.
# Repeat this process until all cities have been visited.
# Return the Number of Provinces:

# After all cities have been checked, return the value of provinces, which now holds the total number of distinct provinces.


class Solution2:
    def findProvinces(self, isConnected) -> int:
        def dfs(city):
            # For each city, mark it as visited and explore its connections
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)

        visited = [False] * len(isConnected)
        provinces = 0

        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces


def main():
    solution = Solution()

    # Example 1
    example1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example1))  # Expected Output: 2

    # Example 2
    example2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example2))  # Expected Output: 3

    # Example 3
    example3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    print(solution.findProvinces(example3))  # Expected Output: 2


# Time Complexity
# Depth First Search (DFS): For a given node, the DFS will explore all of its neighbors. In the worst case, we may end up visiting all nodes in the graph starting from a single node. Hence, the DFS complexity is O(n), where (n) is the number of nodes.

# Overall Time Complexity: For each node, we might call DFS once (if that node is not visited before). Thus, the overall time complexity is O(n^2), with the DFS call being nested inside a loop that iterates over all nodes. In dense graphs where each node is connected to every other node, we will reach this upper bound.


# Space Complexity
# Visited Array: This is an array of size (n) (the number of nodes), so its space requirement is O(n).
# Recursive Call Stack: In the worst case, if all cities are connected in a linear manner (like a linked list), the maximum depth of recursive DFS calls will be (n). Hence, the call stack will take O(n) space.
# Overall Space Complexity: The dominant space-consuming factors are the visited array and the recursive call stack. Hence, the space complexity is O(n).
