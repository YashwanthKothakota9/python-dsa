# Breadth-First Search (BFS) is a graph traversal algorithm that explores a graph's vertices (nodes) level by level. It starts from a selected source node and moves outward to visit all the nodes at the same distance from the source before moving on to nodes at the following distance level.

# BFS is particularly useful for finding the shortest path in unweighted graphs and for systematically exploring graphs.

# Here is a complete description of the Breadth-First Search algorithm:

# 1. Use a Queue

# BFS uses a queue to keep track of the nodes to be visited. The queue follows the First-In-First-Out (FIFO) principle, where the first node inserted in the queue will be the first one to be removed (dequeue).
# 2. Initialization:

# Start by selecting a source node to begin the traversal.
# Create an empty queue to hold the nodes to be visited.
# Mark the source node as visited and enqueue it into the queue.
# 3. Traversal:

# While the queue is not empty, continue the following steps:
# Dequeue a node from the front of the queue (let's call it the "current node").
# Process the current node (print it, perform some operation, etc.).
# Enqueue all the unvisited neighbors of the current node into the queue.
# Mark each enqueued neighbor as visited.
# 4. Termination:

# The BFS algorithm continues until the queue becomes empty, meaning all reachable nodes from the source node have been visited.


from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def BFS(self, startVertex):
        visited = [False] * self.V
        q = deque()
        
        visited[startVertex] = True
        q.append(startVertex)
        
        while q:
            currVertex = q.popleft()
            print(currVertex, end=' ')
            
            for neighbor in self.adjList[currVertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

if __name__ == '__main__':
    graph = Graph(6)
    
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 3)
    graph.addEdge(2, 4)
    graph.addEdge(3, 4)
    graph.addEdge(3, 5)

    print("Breadth-First Traversal starting from vertex 0:")
    graph.BFS(0)

# Complexity analysis
# The time and space complexity of Breadth-First Search (BFS) depends on the size of the graph and the way it is represented. Let's analyze the complexities:

# 1. Time Complexity:

# Visiting a vertex takes O(1) time as we dequeue it from the queue in constant time.
# Exploring the neighbors of a vertex takes O(1) time per neighbor, as we have to traverse its adjacency list once.
# In the worst case, we visit all the vertices at least once, which takes O(V) time. Additionally, for each vertex, we explore all its neighbors once, which takes O(E) time in total (sum of the sizes of all adjacency lists).
# Hence, the overall time complexity of BFS is: O(V+E)
# 2. Space Complexity:

# The space required to store the graph using an adjacency list representation is O(V+E), as we need to store each vertex and its corresponding edges.
# The space required for the queue in BFS is O(V) in the worst case, as all the vertices can be in the queue at once.
# Since the space occupied by the queue is dominant in the overall space complexity, the space complexity of BFS is: O(V)
# BFS is generally efficient for searching and traversal when the graph is not too dense. For sparse graphs, where E is much smaller than V^2, the time complexity becomes almost linear, making BFS a reasonable choice for many practical applications.

# BFS guarantees it visits nodes according to their distance from the source node. It is an efficient algorithm to find the shortest path in unweighted graphs. Additionally, BFS can find connected components, detect cycles, and solve graph-related problems. However, it may consume more memory than DFS, especially in graphs with a significant or infinite branching factor.