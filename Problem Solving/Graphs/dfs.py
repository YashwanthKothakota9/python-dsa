# Depth-First Search (DFS) is a graph traversal algorithm that explores all the nodes in a graph by systematically visiting as far as possible along each branch before backtracking. It operates on both directed and undirected graphs and can be implemented using recursion or an explicit stack data structure.

# DFS starts from a selected source node (or a starting point) and explores as deeply as possible along each branch before backtracking. The algorithm visits nodes in a depth ward motion until it reaches a leaf node with no unexplored neighbors. At that point, it backtracks and explores other unexplored branches.

# Here's a step-by-step explanation of the DFS algorithm:

# 1. Initialization:

# Choose a starting node as the source node.
# Create a data structure to keep track of visited nodes (e.g., an array or a hash set) and mark the source node as visited.
# 2. Visit the Current Node:

# Process the current node (e.g., print its value or perform any other operation you need to do).
# 3. Recursive Approach (Using Recursion):

# For each unvisited neighbor of the current node:
# Recursively call the DFS function with the neighbor as the new current node.
# Mark the neighbor as visited.
# 4. Stack-Based Approach (Using an Explicit Stack):

# Push the starting node onto the stack.
# While the stack is not empty:
# Pop a node from the stack (current node).
# Process the current node (e.g., print its value or perform any other operation you need to do).
# For each unvisited neighbor of the current node:
# Push the unvisited neighbor onto the stack.
# Mark the neighbor as visited.
# 5. Backtracking:

# If there are no more unvisited neighbors for the current node, backtrack by returning from the recursive function (if recursion) or popping nodes from the stack until a node with unvisited neighbors is found (if using an explicit stack).
# 6. Termination:

# The DFS algorithm terminates when all nodes reachable from the source node have been visited. This means that all connected components of the graph have been explored.



class Graph:
    def __init__(self,  V):
        self.vertices = V
        self.adjList = [[] for _ in range(V)]
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def DFS(self, start):
        visited = [False] * self.vertices
        stack = []
        
        stack.append(start)
        visited[start] = True
        
        while stack:
            curr = stack.pop()
            print(curr)
            
            for neighbor in self.adjList[curr]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

g = Graph(7)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

print("DFS Traversal starting from vertex 0:")
g.DFS(0)



# Complexity analysis
# The time and space complexity of Depth-First Search (DFS) depend on the size and structure of the graph being traversed. Let's analyze the complexity of DFS:

# 1. Time Complexity:

# In the worst case, DFS once visits all nodes and edges in the graph. For a graph with V vertices (nodes) and E edges, the time complexity of DFS is O(V+E)

# The time complexity can be further broken down as follows:

# Visiting a node (marking it as visited and processing it) takes O(1) time.

# Exploring all neighbors of a node takes O(d) time, where 'd' is the average degree of nodes in the graph. In the worst case, 'd' can be as high as V-1 (complete graph).

# So, the time complexity can be approximated as O(V) for exploring all neighbors of one node.
# In summary, the overall time complexity of DFS is: 

# 2. Space Complexity:

# The space complexity of DFS is determined by the space needed to store information about the nodes during the traversal. The primary sources of space usage are the recursion stack (if using recursion) or the explicit stack data structure (if using an iterative approach).
# In the worst case, the maximum depth of the recursion stack (or the maximum number of nodes stored in the stack) is the height of the deepest branch of the graph. For a graph with a single connected component, this height can be O(v-1) (when all nodes are connected in a straight line).
# The space complexity of the recursion stack in the worst case is O(V). Additionally, if an explicit stack is used, its space complexity would also be  in the worst case.
# In summary, the overall space complexity of DFS is O(V) due to the recursion stack or the explicit stack.

# DFS can be used for various applications, such as finding connected components, detecting cycles in the graph, topological sorting, and solving problems like maze exploration or finding paths between nodes.

# It's essential to be cautious about infinite loops when traversing graphs that may have cycles. To avoid this, the algorithm must keep track of visited nodes and avoid revisiting nodes that have already been explored.

# Overall, DFS is a powerful graph traversal algorithm that can efficiently explore the entire graph and is widely used in many graph-related problems.