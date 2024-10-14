# We are given an undirected graph that has the characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.

# Example 1:

# Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
# Output:[1, 2]
# Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the height of the trees with roots '1' or '2' is three which is the minimum.

# Example 2:

# Input: vertices: 4, Edges: [[0, 1], [0, 2], [2, 3]]
# Output:[0, 2]
# Explanation: Choosing '0' or '2' as roots give us MHTs. In the below diagram, we can see that the height of the trees with roots '0' or '2' is three which is minimum.

# Example 3:

# Input: vertices: 4, Edges: [[0, 1], [1, 2], [1, 3]]
# Output:[1]


# Solution
# The key intuition behind solving this problem is based on the definition of a tree's height: the height of a tree is the number of edges on the longest path between the root and any leaf. So, an MHT is a tree that minimizes this longest path.

# Imagine we have a longest path P in the tree. The path P has two ends; let's call them end A and end B. Now, let's consider what the root of an MHT can be:

# If we select a root that is not on the path P, the height of the tree would at least be the length of P, because there would be a path from the root to either A or B that is longer than P (as it includes P plus some additional edges). Therefore, the root of the MHT must be on P.

# If the root is on P, but not in the middle of P, then the height of the tree will be larger than if we selected the root in the middle of P, because the longest path will be from the root to either end of P. Therefore, the root of the MHT must be in the middle of P.

# So, the problem of finding the MHT root(s) reduces to finding the middle node(s) of the longest path in the tree.

# We can find the middle node(s) of the longest path by using an algorithm called 'leaf pruining'. Let's look into this.

# From the above discussion, we can deduce that the leaves can’t give us MHT, hence, we can remove them from the graph and remove their edges too. Once we remove the leaves, we will have new leaves. Since these new leaves can’t give us MHT, we will repeat the process and remove them from the graph too. We will prune the leaves until we are left with one or two nodes which will be our answer and the roots for MHTs.

# The algorithm works because when you trim leaves, you're essentially trimming the ends of all the longest paths in the tree. If there's one longest path, you're trimming it from both ends, and if there are multiple longest paths, you're trimming them all. Eventually, you're left with one or two nodes, which must be the middle of the longest path(s), and those are the roots of the MHTs.

# We can implement the above process using the topological sort. Any node with only one edge (i.e., a leaf) can be our source and, in a stepwise fashion, we can remove all sources from the graph to find new sources. We will repeat this process until we are left with one or two nodes in the graph, which will be our answer.

# This Java algorithm is used to find the root nodes of the Minimum Height Trees (MHTs) in a graph. An MHT is a tree rooted at a specific node that minimizes the tree's height. In a graph with 'n' nodes, there can be one or two MHTs.

# Here's a breakdown of the algorithm:

# It starts by checking if the number of nodes is less than or equal to 0, returning an empty list if true, as there would be no trees in the graph. If the graph contains only one node, it returns that single node as an MHT.

# Next, it initializes two HashMaps, inDegree to store the count of incoming edges for every vertex and graph as an adjacency list representation of the graph. It populates these HashMaps with initial values.

# The algorithm then constructs the graph. As it's an undirected graph, each edge connects two nodes bi-directionally, meaning it adds a link for both nodes and increments the in-degrees of the two nodes.

# The algorithm finds all leaf nodes (nodes with only one in-degree) and adds them to a queue.

# Next, it iteratively removes the leaf nodes level by level, subtracting one from the in-degree of each leaf node's children. If a child node becomes a leaf node as a result, it is added to the queue of leaf nodes. This process repeats until the graph has been reduced to one or two nodes, which represent the roots of the MHTs.

# Finally, the algorithm adds the remaining nodes in the leaves queue to minHeightTrees and returns this list. These nodes are the roots of the MHTs in the graph.

from collections import deque


class Solution:
    def findTrees(self, nodes, edges):
        if nodes <= 0:
            return []

        # with only one node, since its in-degrees will be 0, therefore, we need to handle it
        # separately
        if nodes == 1:
            return [0]

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(nodes)}  # count of incoming edges
        graph = {i: [] for i in range(nodes)}  # adjacency list graph

        # b. Build the graph
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            # since this is an undirected graph, therefore, add a link for both the nodes
            graph[n1].append(n2)
            graph[n2].append(n1)
            # increment the in-degrees of both the nodes
            inDegree[n1] += 1
            inDegree[n2] += 1

        # c. Find all leaves i.e., all nodes with 1 in-degrees
        leaves = deque()
        for key in inDegree:
            if inDegree[key] == 1:
                leaves.append(key)

        # d. Remove leaves level by level and subtract each leave's children's in-degrees.
        # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
        # Any node that has already been a leaf cannot be the root of a minimum height tree,
        # because its adjacent non-leaf node will always be a better candidate.
        totalNodes = nodes
        while totalNodes > 2:
            leavesSize = len(leaves)
            totalNodes -= leavesSize
            for i in range(0, leavesSize):
                vertex = leaves.popleft()
                # get the node's children to decrement their in-degrees
                for child in graph[vertex]:
                    inDegree[child] -= 1
                    if inDegree[child] == 1:
                        leaves.append(child)

        return list(leaves)


def main():
    sol = Solution()
    print("Roots of MHTs: " +
          str(sol.findTrees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(sol.findTrees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(sol.findTrees(4, [[1, 2], [1, 3]])))


main()


# Time Complexity
# In step ‘d’, each node can become a source only once and each edge will be accessed and removed once. Therefore, the time complexity of the above algorithm will be O(V+E), where ‘V’ is the total nodes and ‘E’ is the total number of the edges.

# Space Complexity
# The space complexity will be O(V+E), since we are storing all of the edges for each node in an adjacency list.
