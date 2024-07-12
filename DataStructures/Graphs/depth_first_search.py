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