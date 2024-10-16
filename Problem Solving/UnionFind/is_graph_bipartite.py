# Given a 2D array graph[][], representing the undirected graph, where graph[u] is an array of nodes that are connected with node u.

# Determine whether a given undirected graph is a bipartite graph.

# The graph is a bipartite graph, if we can split the set of nodes into two distinct subsets such that no two nodes within the same subset are adjacent (i.e., no edge exists between any two nodes within a single subset).

# Example 1:
# Input: graph = [[1,3], [0,2], [1,3], [0,2]]
# Expected Output: true
# Justification: The nodes can be divided into two groups: {0, 2} and {1, 3}. No two nodes within each group are adjacent, thus the graph is bipartite.
# Example 2:
# Input: graph = [[1], [0], [3], [2]]
# Expected Output: true
# Justification: The graph is a simple chain of 4 nodes. It's clearly bipartite as we can have {0, 2} and {1, 3} as the two subsets.
# Example 3:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Expected Output: false
# Justification: We found that edges (1, 2), (0, 3), and (2, 3) connect nodes within the same set, which violates the condition for a bipartite graph where each edge must connect nodes in different subsets. Thus, there's no way to divide this graph into two subsets that satisfy the bipartite condition.

# Algorithm Description
# The algorithm for determining if a graph is bipartite uses the Union-Find data structure, enhanced with path compression and union by rank. The primary goal is to ensure that no two adjacent nodes are in the same set, which would indicate that the graph is not bipartite.

# Initially, each node is its own parent, and all ranks are set to zero. The algorithm then iterates through each node and its neighbors. For each node, it selects the first neighbor as a representative to which other neighbors will be compared. This is done to ensure that all neighbors of a node are placed in the opposite set. By attempting to union each neighbor with the first neighbor, we effectively check if all neighbors can be grouped together in a way that maintains the bipartite property.

# If, during this process, a neighbor is found to be in the same set as the current node (i.e., they have the same root), it indicates that the graph is not bipartite, and the function returns false. If no such conflict is detected after processing all nodes, the graph is bipartite, and the function returns true. This method ensures efficient and accurate detection of bipartite graphs using the Union-Find structure.

# Step-by-Step Algorithm
# Initialization:

# Create arrays parent and rank of size equal to the number of nodes.
# Initialize each node as its own parent in the parent array.
# Initialize the rank array with zeros.
# Iterate through each node:

# For each node u:
# If u has no edges, continue to the next node.
# Find the root of node u using the find operation.
# Select the first neighbor of u as the representative neighbor.
# Check neighbors and perform union operations:

# For each neighbor v of node u:
# If the root of u is the same as the root of v, a conflict is detected, and the graph is not bipartite. Return false.
# Otherwise, perform a union operation between the first neighbor and the current neighbor v.
# Return result:

# If no conflicts are found after processing all nodes, return true.
# Algorithm Walkthrough
# For the input [[1,3], [0,2], [1,3], [0,2]]:

# Initialization:

# parent = [0, 1, 2, 3]
# rank = [0, 0, 0, 0]
# First Node (u = 0):

# Neighbors: [1, 3]
# find(0): Returns 0 (root of 0 is 0)
# First neighbor: 1
# Neighbor (v = 1):
# find(1): Returns 1 (root of 1 is 1)
# Roots of 0 and 1 are different. Perform union(1, 1):
# find(1): Returns 1
# find(1): Returns 1
# Roots are the same. No change in parent and rank.
# Neighbor (v = 3):
# find(3): Returns 3 (root of 3 is 3)
# Roots of 0 and 3are different. Perform union(1, 3):
# find(1): Returns 1
# find(3): Returns 3
# rank[1] == rank[3], so parent[3] = 1 and rank[1]++. Updated parent = [0, 1, 2, 1], rank = [0, 1, 0, 0].
# Second Node (u = 1):

# Neighbors: [0, 2]
# find(1): Returns 1 (root of 1 is 1)
# First neighbor: 0
# Neighbor (v = 0):
# find(0): Returns 0 (root of 0 is 0)
# Roots of 1 and 0 are different. Perform union(0, 0):
# find(0): Returns 0
# find(0): Returns 0
# Roots are the same. No change in parent and rank.
# Neighbor (v = 2):
# find(2): Returns 2 (root of 2 is 2)
# Roots are different. Perform union(0, 2):
# find(0): Returns 0
# find(2): Returns 2
# rank[0] == rank[2], so parent[2] = 0 and rank[0]++. Updated parent = [0, 1, 0, 1], rank = [1, 0, 0, 0].
# Third Node (u = 2):

# Neighbors: [1, 3]
# find(2): Returns 0 (root of 2 is 0)
# First neighbor: 1
# Neighbor (v = 1):
# find(1): Returns 1 (root of 1 is 1)
# Roots are different. Perform union(1, 1):
# find(1): Returns 1
# find(1): Returns 1
# Roots are the same. No change in parent and rank.
# Neighbor (v = 3):
# find(3): Returns 1 (root of 3 is 1)
# Roots are different. Perform union(1, 3):
# find(1): Returns 1
# find(3): Returns 1
# Roots are the same. No change in parent and rank.
# Fourth Node (u = 3):

# Neighbors: [0, 2]
# find(3): Returns 1 (root of 3 is 1)
# First neighbor: 0
# Neighbor (v = 0):
# find(0): Returns 0 (root of 0 is 0)
# Roots are different. Perform union(0, 0):
# find(0): Returns 0
# find(0): Returns 0
# Roots are the same. No change in parent and rank.
# Neighbor (v = 2):
# find(2): Returns 0 (root of 2 is 0)
# Roots are different. Perform union(0, 2):
# find(0): Returns 0
# find(2): Returns 2
# Roots are the same. No change in parent and rank.
# No conflict is detected. So, the graph is not bipartite.


class Solution:
    def __init__(self) -> None:
        self.parent = []
        self.rank = []

    def isBipartite(self, graph):
        self.parent = list(range(len(graph)))
        self.rank = [0]*len(graph)

        def find(node):
            if self.parent[node] != node:
                self.parent[node] = find(self.parent[node])  # Path compression
            return self.parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                # Union by rank
                if self.rank[root1] > self.rank[root2]:
                    self.parent[root2] = root1
                elif self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1

        for u in range(len(graph)):
            if not graph[u]:  # No edges for this node
                continue
            parentU = find(u)  # Find the parent set for u
            firstNeighbor = graph[u][0]  # Take the first neighbor

            # Union the rest of u's neighbors to the first neighbor's set
            for v in graph[u]:
                if parentU == find(v):
                    return False  # If u and v belong to the same set
                union(firstNeighbor, v)  # Union v with the first neighbor

        return True


solution = Solution()
print(solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
print(solution.isBipartite([[1], [0], [3], [2]]))  # True
print(solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False


# Time Complexity
# Initializing the parent and rank arrays takes O(N) time, where N is the number of nodes in the graph.
# Processing each node:

# For each node u, the code checks its neighbors.
# Finding the parent set of each node using the Find method takes nearly constant time,O(alpha(N)) , where α is the inverse Ackermann function, which grows very slowly.
# Performing the union operation also takes nearly constant time, O(alpha(N)).
# The nested loop iterates over all edges in the graph. If we denote the total number of edges by E, then iterating over all edges will take O(E) time.
# Total Time Complexity:

# Combining all, the overall time complexity is O((N+E)*α(N)), which simplifies to O(N+E) in practical scenarios because α(N) is very small and can be considered a constant.
# Space Complexity
# Space for parent and rank arrays:

# The space required for the parent array is O(N).
# The space required for the rank array is O(N).
# Total Space Complexity:

# The overall space complexity is O(N), which is needed for the parent and rank arrays.
