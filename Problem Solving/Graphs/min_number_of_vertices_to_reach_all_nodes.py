# Given a directed acyclic graph with n nodes labeled from 0 to n-1, determine the smallest number of initial nodes such that you can access all the nodes by traversing edges. Return these nodes.

# Examples
# Example 1:
# Input:
# n = 6
# edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Expected Output: [0,3]
# Justification: Starting from nodes 0 and 3, you can reach all other nodes in the graph. Starting from node 0, you can reach nodes 1, 2, and 5. Starting from node 3, you can reach nodes 4 and 2 (and by extension 5).

# Example 2:
# Input:
# n = 3
# edges = [[0,1],[2,1]]
# Expected Output: [0,2]

# Justification: Nodes 0 and 2 are the only nodes that don't have incoming edges. Hence, you need to start from these nodes to reach node 1.

# To solve the problem of determining the minimum number of vertices needed to reach all nodes in a directed graph, we focus on the concept of "in-degree" which represents the number of incoming edges to a node. In a directed graph, if a node doesn't have any incoming edges (in-degree of 0), then it means that the node cannot be reached from any other node. Hence, such nodes are mandatory starting points to ensure that every node in the graph can be reached. Our algorithm thus identifies all nodes with an in-degree of 0 as they are potential starting points to traverse the entire graph.

# Steps:

# Graph Representation: Begin by representing the graph using an adjacency list or a similar data structure.

# In-Degree Calculation: Compute the in-degree for all the nodes. The in-degree of a node is the number of edges coming into it. This can be done by initializing an array to keep track of in-degrees for each node and iterating over the edges to update the in-degree counts.

# Result Gathering: Iterate over the computed in-degrees. Nodes with an in-degree of 0 don't have any incoming edges and thus are part of our result set as they serve as starting points.


from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n:int, edges:List[List[int]]) -> List[int]:
        # Create a set to store nodes with incoming edges
        nodes_with_incoming = set()
        
        #populate the set
        for _, to_node in edges:
            nodes_with_incoming.add(to_node)
        
        # Return nodes without incoming edges
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


# Time Complexity:
# Initialization: Initializing the set for all nodes in the graph takes (O(n)), where (n) is the number of nodes.

# Processing Edges: For every edge ([u, v]), we are simply checking and potentially removing the node (v) from our set. Since we do a constant amount of work for each edge, this step takes (O(e)) time, where (e) is the number of edges.

# Thus, the overall time complexity is the sum of the above two steps, i.e., (O(n + e)). In the worst case (a complete graph), every node is connected to every other node, making (e = n^2), leading to a worst-case time complexity of (O(n^2)). However, this is not a typical scenario, and in most real-world graphs, (e) is often linear or close to linear with respect to (n). Therefore, (O(n + e)) is a more informative measure.

# Space Complexity:
# Set for Nodes: The set that we're using to keep track of nodes which do not have any incoming edges will, at most, contain all nodes. This gives us a space complexity of (O(n)).

# Graph Representation: Though we are given the edges as an input, if we consider the space used by this representation, it will be (O(e)) for the edges.

# However, note that since we are not using any additional data structures that scale with the size of the graph other than the set for nodes, our primary concern is the set's space. Thus, the dominant term here is (O(n)).

# So, the overall space complexity is (O(n)).

# In summary:

# Time Complexity: (O(n + e))
# Space Complexity: (O(n))