from typing import List, Set

class Solution:
    def initializeGraph(self, numVertices: int) -> None:
        self.V: int = numVertices
        self.adj: List[List[int]] = [[] for _ in range(self.V)]
    
    def addEdge(self, u:int, v:int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def DFSExe(self, startNode: int, visited: Set[int], depthFirstSearch: List[int]) -> None:
        visited.add(startNode)
        depthFirstSearch.append(startNode)
        for neighbour in self.adj[startNode]:
            if neighbour not in visited:
                self.DFSExe(neighbour, visited, depthFirstSearch)
    
    def DFS(self, args: List[List[int]], n: int, first: int) -> List[int]:
        self.initializeGraph(n)
        depthFirstSearch: List[int] = []
        
        for num in args:
            self.addEdge(num[0], num[1])
            
        self.DFSExe(first, set(), depthFirstSearch)
        return depthFirstSearch

graph = Solution()
args: List[List[int]] = [[1,2],[1,5],[2,5],[1,4],[4,3],[3,5]]
n: int = len(args)
print("DFS traversal:", end=" ")
print(graph.DFS(args,n,1))