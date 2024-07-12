from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def BFS(self, start):
        visited = [False] * self.V
        q = deque()
        
        visited[start] = True
        q.append(start)
        
        while q:
            curr = q.popleft()
            print(curr, end=" ")
            
            for neighbour in self.adjList[curr]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)

if __name__ == "__main__":
    graph = Graph(6)  # Create a graph with 6 vertices

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

# Visiting a vertex takes  time as we dequeue it from the queue in constant time.
# Exploring the neighbors of a vertex takes  time per neighbor, as we have to traverse its adjacency list once.
# In the worst case, we visit all the vertices at least once, which takes  time. Additionally, for each vertex, we explore all its neighbors once, which takes  time in total (sum of the sizes of all adjacency lists).
# Hence, the overall time complexity of BFS is: 
# 2. Space Complexity:

# The space required to store the graph using an adjacency list representation is , as we need to store each vertex and its corresponding edges.
# The space required for the queue in BFS is  in the worst case, as all the vertices can be in the queue at once.
# Since the space occupied by the queue is dominant in the overall space complexity, the space complexity of BFS is: O(V)