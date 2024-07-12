# Given a directed acyclic graph with n nodes labeled from 0 to n-1, determine the smallest number of initial nodes such that you can access all the nodes by traversing edges. Return these nodes.

# Examples
# Input:

# n = 6
# edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Expected Output: [0,3]

# Justification: Starting from nodes 0 and 3, you can reach all other nodes in the graph. Starting from node 0, you can reach nodes 1, 2, and 5. Starting from node 3, you can reach nodes 4 and 2 (and by extension 5).

# Input:

# n = 3
# edges = [[0,1],[2,1]]
# Expected Output: [0,2]

# Justification: Nodes 0 and 2 are the only nodes that don't have incoming edges. Hence, you need to start from these nodes to reach node 1.

# Input:

# n = 5
# edges = [[0,1],[2,1],[3,4]]
# Expected Output: [0,2,3]

# Justification: Node 1 can be reached from both nodes 0 and 2, but to cover all nodes, you also need to start from node 3.

# To solve the problem of determining the minimum number of vertices needed to reach all nodes in a directed graph, we focus on the concept of "in-degree" which represents the number of incoming edges to a node. In a directed graph, if a node doesn't have any incoming edges (in-degree of 0), then it means that the node cannot be reached from any other node. Hence, such nodes are mandatory starting points to ensure that every node in the graph can be reached. Our algorithm thus identifies all nodes with an in-degree of 0 as they are potential starting points to traverse the entire graph.
# Time Complexity: (O(n + e))
# Space Complexity: (O(n))

from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n:int, edges:List[List[int]]) -> List[int]:
        nodes_with_incoming = set()
        for _,to_node in edges:
            nodes_with_incoming.add(to_node)
        return [i for i in range(n) if i not in nodes_with_incoming]

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    edges1 = [[0,1], [0,2], [2,5], [3,4], [4,2]]
    print(solution.findSmallestSetOfVertices(6, edges1))  # Expected: [0, 3]
    
    edges2 = [[0,1], [3,1], [1,2]]
    print(solution.findSmallestSetOfVertices(4, edges2))  # Expected: [0, 3]
    
    edges3 = [[2,0], [3,2]]
    print(solution.findSmallestSetOfVertices(4, edges3))  # Expected: [1, 3]
