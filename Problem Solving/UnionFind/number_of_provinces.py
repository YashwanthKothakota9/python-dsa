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
