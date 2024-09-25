from collections import defaultdict


class Solution:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function to perform topological sort
    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topologicalSortUtil(neighbor, visited, stack)

        # Push current vertex to stack which stores the result
        stack.append(v)

    # The function to do Topological Sort
    def topologicalSort(self):
        stack = []

        # Mark all the vertices as not visited
        visited = [False]*self.vertices

        # Call the recursive helper function to store Topological Sort
        # starting from all vertices one by one
        for i in range(self.vertices):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack in reverse order
        print(stack[::-1])


# Create a graph given in the above diagram
g = Solution(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Topological sort of the given graph:")
g.topologicalSort()

# Complexity Analysis:
# Time Complexity: The time complexity of the DFS-based topological sorting algorithm is O(V+E), where (V) is the number of vertices and (E) is the number of edges in the graph. This is because each vertex and edge is processed exactly once.
# Space Complexity: The space complexity is O(V) due to the stack and the visited array used to keep track of the visited vertices. The adjacency list representation of the graph also requires O(V+E) space.
