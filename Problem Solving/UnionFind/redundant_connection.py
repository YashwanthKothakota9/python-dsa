# Given an undirected graph containing 1  to n nodes. The graph is represented by a 2D array of edges, where edges[i] = [ai, bi], represents an edge between ai, and bi.

# Identify one edge that, if removed, will turn the graph into a tree.

# A tree is a graph that is connected and has no cycles.

# Assume that the graph is always reducible to a tree by removing just one edge.

# If there are multiple answers, return the edge that occurs last in the input.

# Examples
# Example 1:
# Input: [[1,2], [1,3], [3,4], [1,4], [1,5]]

# Expected Output: [1,4]
# Justification: The edge [1,4] is redundant because removing it will eliminate the cycle 1-3-4-1 while keeping the graph connected.
# Example 2:
# Input: [[1,2], [2,3], [3,1], [3,4]]

# Expected Output: [3,1]
# Justification: The edge [3,1] creates a cycle 1-2-3-1. Removing it leaves a tree with no cycles.
# Example 3:
# Input: [[1,2], [2,3], [3,4], [4,2], [5,6]]

# Expected Output: [4,2]
# Justification: The edge [4,2] adds a cycle 2-3-4-2 in one part of the graph. Removing this edge breaks the cycle, and the remaining graph is a tree.

# The solution to this problem employs the Union-Find algorithm, which is effective for cycle detection in graphs. Initially, each node is considered as a separate set. As we iterate through the edges of the graph, we use the Union-Find approach to determine if the nodes connected by the current edge are already part of the same set. If they are, it indicates the presence of a cycle, and this edge is the redundant one. Otherwise, unite these two sets, meaning connect the nodes without forming a cycle. This approach focuses on progressively merging nodes into larger sets while keeping an eye out for the edge that connects nodes already in the same set.


# Step-by-Step Algorithm
# Initialization:

# Create a parent array of size edges.Length + 1 (to accommodate 1-based node indexing).
# Initialize each element in the parent array to be its own parent.
# Process Each Edge:

# For each edge in the input edges array:
# Extract the two nodes, node1 and node2.
# Use the find operation to determine the root of node1.
# Use the find operation to determine the root of node2.
# If both nodes have the same root, a cycle is detected, and the current edge is redundant. Return this edge.
# Otherwise, use the union operation to merge the sets containing node1 and node2.
# Return the Result:

# If no redundant connection is found (which should not happen as per the problem statement), return an empty array.


class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges)+1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(node1, node2):
            parent[find(node1)] = find(node2)

        for edge in edges:
            node1, node2 = edge
            if find(node1) == find(node2):
                return edge  # Redundant connection found
            union(node1, node2)

        return []


if __name__ == '__main__':
    solution = Solution()

    # Test the algorithm with the three example inputs
    example1 = [[1, 2], [1, 3], [3, 4], [1, 4], [1, 5]]
    example2 = [[1, 2], [2, 3], [3, 1], [3, 4]]
    example3 = [[1, 2], [2, 3], [3, 4], [4, 2], [5, 6]]

    print("Example 1:", solution.findRedundantConnection(example1))
    print("Example 2:", solution.findRedundantConnection(example2))
    print("Example 3:", solution.findRedundantConnection(example3))


# Time Complexity
# Initialization:

# Initializing the parent array takes O(N) time, where (N) is the number of nodes.
# Find Operation:

# The find operation with path compression has an amortized time complexity of O(logN), which is almost equal to O(alpha(N)), where alpha(N) is the inverse Ackermann function, which is very close to constant.

# Union Operation:

# The union operation involves two find operations and one assignment, leading to a time complexity of O(alpha(N)) per union.

# Processing Edges:

# For each edge, we perform two find operations and one union operation. Since there are (E) edges, the total time complexity for processing all edges is O(N*alpha(N)), where N is a number of edges.
# The total time complexity is O(N+N*alpha(N)), which is equal to O(N*alpha(N)).

# Space Complexity
# The parent array requires O(N) space to store the parent of each node.
