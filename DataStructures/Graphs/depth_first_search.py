class Graph:
    def __init__(self, V):
        self.vertices = V
        self.adjList = [[] for _ in range(V)]
    
    def addEdge(self,u,v):
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
            
            for neighbour in self.adjList[curr]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True

g = Graph(7)
g.addEdge(0,1)
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

# In the worst case, DFS once visits all nodes and edges in the graph. For a graph with V vertices (nodes) and E edges, the time complexity of DFS is 

# The time complexity can be further broken down as follows:

# Visiting a node (marking it as visited and processing it) takes  time.

# Exploring all neighbors of a node takes  time, where 'd' is the average degree of nodes in the graph. In the worst case, 'd' can be as high as  (complete graph).

# So, the time complexity can be approximated as  for exploring all neighbors of one node.
# In summary, the overall time complexity of DFS is: 

# 2. Space Complexity:

# The space complexity of DFS is determined by the space needed to store information about the nodes during the traversal. The primary sources of space usage are the recursion stack (if using recursion) or the explicit stack data structure (if using an iterative approach).
# In the worst case, the maximum depth of the recursion stack (or the maximum number of nodes stored in the stack) is the height of the deepest branch of the graph. For a graph with a single connected component, this height can be  (when all nodes are connected in a straight line).
# The space complexity of the recursion stack in the worst case is . Additionally, if an explicit stack is used, its space complexity would also be  in the worst case.
# In summary, the overall space complexity of DFS is  due to the recursion stack or the explicit stack.