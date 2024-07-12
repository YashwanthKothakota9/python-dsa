from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool: # type: ignore
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node):
            if node == end:
                return True
            
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited and dfs(neighbour):
                    return True
            return False
        return dfs(start)


sol = Solution()
print(sol.validPath(4, [[0,1],[1,2],[2,3]], 0, 3))  # true
print(sol.validPath(4, [[0,1],[2,3]], 0, 3))      # false
print(sol.validPath(5, [[0,1],[3,4]], 0, 4))      # false
