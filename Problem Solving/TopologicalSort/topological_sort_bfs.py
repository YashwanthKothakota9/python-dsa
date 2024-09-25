# Topological Sort Using BFS (Kahn's Algorithm)

# Kahn's Algorithm for topological sorting uses BFS to process nodes in a way that respects the dependencies. The algorithm works by repeatedly removing nodes with no incoming edges and recording them. This ensures that each node is only processed after all its dependencies have been processed.

# Step-by-Step Algorithm
# Initialization:

# Create an in-degree array to keep track of the number of incoming edges for each vertex.
# Initialize the in-degree of all vertices to 0.
# Create a queue to store all vertices with in-degree 0.
# Calculate In-degree:

# For each vertex, iterate through its adjacency list and increase the in-degree of its neighbors by 1.
# Enqueue Vertices with In-degree 0:

# Iterate through the in-degree array and enqueue all vertices with in-degree 0 into the queue.
# Process Vertices:

# While the queue is not empty:
# Dequeue a vertex from the queue.
# Add the dequeued vertex to the topological order list.
# For each neighbor of the dequeued vertex:
# Decrease the in-degree of the neighbor by 1.
# If the in-degree of the neighbor becomes 0, enqueue the neighbor.
# Check for Cycles:

# If the number of vertices in the topological order list is less than the total number of vertices, there is a cycle in the graph, and topological sorting is not possible.
# Output the Topological Order:

# Print or return the topological order list.


# Algorithm Walkthrough
# Consider the following directed acyclic graph (DAG):

#     5 → 2
#     5 → 0
#     4 → 0
#     4 → 1
#     2 → 3
#     3 → 1
# Initialization:

# inDegree = [0, 0, 0, 0, 0, 0]
# queue = []
# topOrder = []
# Calculate In-degree:

# For vertex 5: inDegree = [1, 0, 1, 0, 0, 0]
# For vertex 4: inDegree = [2, 1, 1, 0, 0, 0]
# For vertex 2: inDegree = [2, 1, 1, 1, 0, 0]
# For vertex 3: inDegree = [2, 2, 1, 1, 0, 0]
# Enqueue Vertices with In-degree 0:

# Vertices with in-degree 0: 4, 5
# queue = [4, 5]
# Process Vertices:

# Dequeue 4:
# topOrder = [4]
# Decrease in-degree of neighbors 0 and 1:
# inDegree = [1, 1, 1, 1, 0, 0]
# No new vertices with in-degree 0.
# queue = [5]
# Dequeue 5:
# topOrder = [4, 5]
# Decrease in-degree of neighbors 2 and 0:
# inDegree = [0, 1, 0, 1, 0, 0]
# Add 2 and 0 to the queue (both now have in-degree 0).
# queue = [2, 0]
# Dequeue 2:
# topOrder = [4, 5, 2]
# Decrease in-degree of neighbor 3:
# inDegree = [0, 1, 0, 0, 0, 0]
# Add 3 to the queue (now has in-degree 0).
# queue = [0, 3]
# Dequeue 0:
# topOrder = [4, 5, 2, 0]
# queue = [3]
# Dequeue 3:
# topOrder = [4, 5, 2, 0, 3]
# Decrease in-degree of neighbor 1:
# inDegree = [0, 0, 0, 0, 0, 0]
# Add 1 to the queue (now has in-degree 0).
# queue = [1]
# Dequeue 1:
# topOrder = [4, 5, 2, 0, 3, 1]
# queue = []
# Check for Cycles:

# The number of vertices in topOrder is equal to the number of vertices in the graph, so there are no cycles.
# Output the Topological Order:

# The topological order is: 4, 5, 2, 0, 3, 1.

from collections import defaultdict, deque


class Solution:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def topological_sort(self):
        in_degree = [0] * self.vertices

        # Calculate in-degrees of all vertices
        for i in range(self.vertices):
            for neighbor in self.adj_list[i]:
                in_degree[neighbor] += 1

        # Create a queue and enqueue all vertices with in-degree 0
        q = deque()
        for i in range(self.vertices):
            if in_degree[i] == 0:
                q.append(i)

        count = 0  # Initialize count of visited vertices
        top_order = []  # List to store the topological order

        # Process vertices in the queue
        while q:
            u = q.popleft()  # Dequeue a vertex
            top_order.append(u)  # Add it to the topological order

            # Iterate through all its neighboring nodes
            for neighbor in self.adj_list[u]:
                # Reduce in-degree by 1
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    # If in-degree becomes 0, add it to the queue
                    q.append(neighbor)

            count += 1  # Increment count of visited vertices

        # Check if there was a cycle
        if count != self.vertices:
            print("There exists a cycle in the graph")
            return

        # Print topological order
        print("Topological sort of the given graph:")
        print(top_order)


# Example usage
g = Solution(6)  # Create a graph with 6 vertices
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()  # Perform topological sort


# Complexity Analysis
# Time Complexity

# Initialization of in-degree array:O(V+E)
# Calculating the in-degree for all vertices involves iterating over all the vertices and their edges.
# Processing vertices: O(V+E)
# Enqueuing and dequeuing vertices takes O(V) time.
# For each vertex, we reduce the in-degree of its neighbors, which takes O(E) time in total.
# Overall, the time complexity is O(V+E) , where (V) is the number of vertices and (E) is the number of edges.

# Space Complexity

# Adjacency list: O(V+E)
# In-degree array: O(V)
# Queue: O(V)
# Topological order list: O(V)
# Overall, the space complexity is O(V+E) .
