# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

# Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.


# Example 1:

# Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
# Output:
# 1) [3, 2, 0, 1]
# 2) [3, 2, 1, 0]
# Explanation: There are two possible orderings of the tasks meeting all prerequisites.
# Example 2:

# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: [0, 1, 2]
# Explanation: There is only possible ordering of the tasks.
# Example 3:

# Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
# Output:
# 1) [0, 1, 4, 3, 2, 5]
# 2) [0, 1, 3, 4, 2, 5]
# 3) [0, 1, 3, 2, 4, 5]
# 4) [0, 1, 3, 2, 5, 4]
# 5) [1, 0, 3, 4, 2, 5]
# 6) [1, 0, 3, 2, 4, 5]
# 7) [1, 0, 3, 2, 5, 4]
# 8) [1, 0, 4, 3, 2, 5]
# 9) [1, 3, 0, 2, 4, 5]
# 10) [1, 3, 0, 2, 5, 4]
# 11) [1, 3, 0, 4, 2, 5]
# 12) [1, 3, 2, 0, 5, 4]
# 13) [1, 3, 2, 0, 4, 5]

# This problem is similar to Tasks Scheduling Order, the only difference is that we need to find all the topological orderings of the tasks.

# At any stage, if we have more than one source available and since we can choose any source, therefore, in this case, we will have multiple orderings of the tasks. We can use a recursive approach with Backtracking to consider all sources at any step.

# Algorithm Walkthrough
# Let's walk through the algorithm using the input Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1].

# Initialization:

# inDegree = {0: 0, 1: 0, 2: 0, 3: 0}
# graph = {0: [], 1: [], 2: [], 3: []}
# Build the Graph:

# Add edges and update in-degrees:
# Add edge 3 -> 2: inDegree = {0: 0, 1: 0, 2: 1, 3: 0}, graph = {0: [], 1: [], 2: [], 3: [2]}
# Add edge 3 -> 0: inDegree = {0: 1, 1: 0, 2: 1, 3: 0}, graph = {0: [], 1: [], 2: [], 3: [2, 0]}
# Add edge 2 -> 0: inDegree = {0: 2, 1: 0, 2: 1, 3: 0}, graph = {0: [], 1: [], 2: [0], 3: [2, 0]}
# Add edge 2 -> 1: inDegree = {0: 2, 1: 1, 2: 1, 3: 0}, graph = {0: [], 1: [], 2: [0, 1], 3: [2, 0]}
# Find All Sources:

# Sources with 0 in-degrees: sources = [3]
# Process each nodes:

# Recursive Call with Source 3:
# Add 3 to sortedOrder: sortedOrder = [3]

# Remove 3 from sources: sources = []

# Decrement in-degrees of children of 3:

# inDegree = {0: 2, 1: 1, 2: 0, 3: 0}
# Add new source 2 to sources: sources = [2]

# Recursive Call with Source 2:
# Add 2 to sortedOrder: sortedOrder = [3, 2]

# Remove 2 from sources: sources = []

# Decrement in-degrees of children of 2:

# inDegree = {0: 1, 1: 0, 2: 0, 3: 0}
# Add new sources 0 and 1 to sources: sources = [0, 1]

# Recursive Call with Source 0:
# Add 0 to sortedOrder: sortedOrder = [3, 2, 0]

# Remove 0 from sources: sources = [1]

# Decrement in-degrees of children of 0 (none)

# Recursive Call with Source 1:
# Add 1 to sortedOrder: sortedOrder = [3, 2, 0, 1]

# Remove 1 from sources: sources = []

# Decrement in-degrees of children of 1 (none)

# sortedOrder contains all tasks: add [3, 2, 0, 1] to orders

# Backtrack from Source 1:
# Remove 1 from sortedOrder: sortedOrder = [3, 2, 0]

# Restore in-degrees: inDegree = {0: 1, 1: 0, 2: 0, 3: 0}

# Backtrack from Source 0:
# Remove 0 from sortedOrder: sortedOrder = [3, 2]

# Restore in-degrees: inDegree = {0: 2, 1: 0, 2: 0, 3: 0}

# Add source 0 back to sources: sources = [0, 1]

# Recursive Call with Source 1:
# Add 1 to sortedOrder: sortedOrder = [3, 2, 1]

# Remove 1 from sources: sources = [0]

# Decrement in-degrees of children of 1 (none)

# Recursive Call with Source 0:
# Add 0 to sortedOrder: sortedOrder = [3, 2, 1, 0]

# Remove 0 from sources: sources = []

# Decrement in-degrees of children of 0 (none)

# sortedOrder contains all tasks: add [3, 2, 1, 0] to orders

# Backtrack from Source 0:
# Remove 0 from sortedOrder: sortedOrder = [3, 2, 1]

# Restore in-degrees: inDegree = {0: 1, 1: 0, 2: 0, 3: 0}

# Backtrack from Source 1:
# Remove 1 from sortedOrder: sortedOrder = [3, 2]

# Restore in-degrees: inDegree = {0: 2, 1: 0, 2: 0, 3: 0}

# Add source 1 back to sources: sources = [0, 1]

# Backtrack from Source 2:
# Remove 2 from sortedOrder: sortedOrder = [3]

# Restore in-degrees: inDegree = {0: 2, 1: 1, 2: 1, 3: 0}

# Add source 2 back to sources: sources = [2]

# Backtrack from Source 3:
# Remove 3 from sortedOrder: sortedOrder = []

# Restore in-degrees: inDegree = {0: 2, 1: 1, 2: 1, 3: 0}

# Add source 3 back to sources: sources = [3]

# Final Orders:
# [3, 2, 0, 1]
# [3, 2, 1, 0]

from collections import deque


class Solution:
    def __init__(self) -> None:
        self.orders = []

    def printOrders(self, tasks, prerequisites):
        sortedOrder = []
        if tasks <= 0:
            return self.orders

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
        graph = {i: [] for i in range(tasks)}  # adjacency list graph

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            inDegree[child] += 1

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        self.print_all_topological_sorts(graph, inDegree, sources, sortedOrder)

        return self.orders

    def print_all_topological_sorts(self, graph, inDegree, sources, sortedOrder):
        if sources:
            for vertex in sources:
                sortedOrder.append(vertex)
                sources_for_next_call = deque(
                    sources)  # make a copy of sources
                # only remove the current source, all other sources should remain in the queue for
                # the next call
                sources_for_next_call.remove(vertex)
                # get the node's children to decrement their in-degrees
                for child in graph[vertex]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        sources_for_next_call.append(child)

                # recursive call to print other orderings from the remaining (and new) sources
                self.print_all_topological_sorts(
                    graph, inDegree, sources_for_next_call, sortedOrder)

                # backtrack, remove the vertex from the sorted order and put all of its children
                # back to consider the next source instead of the current vertex
                sortedOrder.remove(vertex)
                for child in graph[vertex]:
                    inDegree[child] += 1

        # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between
        # tasks, or we have not processed all the tasks in this recursive call
        if len(sortedOrder) == len(inDegree):
            self.orders.append(sortedOrder.copy())


def main():
    sol = Solution()
    print("Task Orders: ")
    result1 = sol.printOrders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    for order in result1:
        print(order)

    print("Task Orders: ")
    result2 = sol.printOrders(3, [[0, 1], [1, 2]])
    for order in result2:
        print(order)

    print("Task Orders: ")
    result3 = sol.printOrders(
        6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
    for order in result3:
        print(order)


if __name__ == "__main__":
    main()


# Time and Space Complexity
# If we don’t have any prerequisites, all combinations of the tasks can represent a topological ordering. As we know, that there can be N! combinations for ‘N’ numbers, therefore the time and space complexity of our algorithm will be O(V! * E) where ‘V’ is the total number of tasks and ‘E’ is the total prerequisites. We need the ‘E’ part because in each recursive call, at max, we remove (and add back) all the edges.
