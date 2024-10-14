# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

# Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

# Examples
# Example 1:

# Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
# Output: [0 1 4 3 2 5]
# Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
# Example 2:

# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: [0, 1, 2]
# Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
# Example 3:

# Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
# Output: []
# Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.


# This problem is similar to Tasks Scheduling, the only difference being that we need to find the best ordering of tasks so that it is possible to schedule them all.


# Step-by-step Algorithm
# Initialize the Graph:

# Create a HashMap inDegree to count the incoming edges for every vertex.
# Create a HashMap graph to represent the adjacency list of the graph.
# Build the Graph:

# For each task, set the initial in-degree to 0 and create an empty adjacency list.
# For each prerequisite pair [parent, child]:
# Add child to the adjacency list of parent.
# Increment the in-degree of child by 1.
# Find All Sources:

# Initialize a queue sources and add all vertices with 0 in-degrees.
# Sort Tasks:

# While sources is not empty:
# Remove a source from the queue, add it to sortedOrder.
# For each child of this source:
# Decrement the child's in-degree by 1.
# If the child's in-degree becomes 0, add it to the sources queue.
# Check for Cyclic Dependencies:

# If the size of sortedOrder is not equal to the number of tasks, return an empty list (indicating a cycle).
# Otherwise, return sortedOrder.
# Algorithm Walkthrough
# Given:

# Tasks = 6
# Prerequisites = [2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
# Initialize:

# inDegree = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# graph = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
# Build the Graph:

# For [2, 5]:
# graph[2].append(5) → graph = {0: [], 1: [], 2: [5], 3: [], 4: [], 5: []}
# inDegree[5]++ → inDegree = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}
# For [0, 5]:
# graph[0].append(5) → graph = {0: [5], 1: [], 2: [5], 3: [], 4: [], 5: []}
# inDegree[5]++ → inDegree = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2}
# For [0, 4]:
# graph[0].append(4) → graph = {0: [5, 4], 1: [], 2: [5], 3: [], 4: [], 5: []}
# inDegree[4]++ → inDegree = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 2}
# For [1, 4]:
# graph[1].append(4) → graph = {0: [5, 4], 1: [4], 2: [5], 3: [], 4: [], 5: []}
# inDegree[4]++ → inDegree = {0: 0, 1: 0, 2: 0, 3: 0, 4: 2, 5: 2}
# For [3, 2]:
# graph[3].append(2) → graph = {0: [5, 4], 1: [4], 2: [5], 3: [2], 4: [], 5: []}
# inDegree[2]++ → inDegree = {0: 0, 1: 0, 2: 1, 3: 0, 4: 2, 5: 2}
# For [1, 3]:
# graph[1].append(3) → graph = {0: [5, 4], 1: [4, 3], 2: [5], 3: [2], 4: [], 5: []}
# inDegree[3]++ → inDegree = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
# Find All Sources:

# Sources are tasks with 0 in-degrees: sources = [0, 1]
# Process Each Source:

# Process 0:
# Remove 0 from sources → sources = [1]
# Add 0 to sortedOrder → sortedOrder = [0]
# For child 5 of 0, decrement inDegree[5] → inDegree[5] = 1
# For child 4 of 0, decrement inDegree[4] → inDegree[4] = 1
# Process 1:
# Remove 1 from sources → sources = []
# Add 1 to sortedOrder → sortedOrder = [0, 1]
# For child 4 of 1, decrement inDegree[4] → inDegree[4] = 0 → Add 4 to sources → sources = [4]
# For child 3 of 1, decrement inDegree[3] → inDegree[3] = 0 → Add 3 to sources → sources = [4, 3]
# Process 4:
# Remove 4 from sources → sources = [3]
# Add 4 to sortedOrder → sortedOrder = [0, 1, 4]
# Process 3:
# Remove 3 from sources → sources = []
# Add 3 to sortedOrder → sortedOrder = [0, 1, 4, 3]
# For child 2 of 3, decrement inDegree[2] → inDegree[2] = 0 → Add 2 to sources → sources = [2]
# Process 2:
# Remove 2 from sources → sources = []
# Add 2 to sortedOrder → sortedOrder = [0, 1, 4, 3, 2]
# For child 5 of 2, decrement inDegree[5] → inDegree[5] = 0 → Add 5 to sources → sources = [5]
# Process 5:
# Remove 5 from sources → sources = []
# Add 5 to sortedOrder → sortedOrder = [0, 1, 4, 3, 2, 5]
# Check for Cyclic Dependencies:

# sortedOrder = [0, 1, 4, 3, 2, 5] contains all tasks.
# Final order of tasks: [0, 1, 4, 3, 2, 5]

from collections import deque


class Solution:
    def findOrder(self, tasks, prerequisites):
        sortedOrder = []
        if tasks <= 0:
            return sortedOrder

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

        # d. For each source, add it to the sortedOrder and subtract one from all of its
        # children's in-degrees if a child's in-degree becomes zero, add it to sources queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between
        # tasks, therefore, we will not be able to schedule all tasks
        if len(sortedOrder) != tasks:
            return []

        return sortedOrder


def main():
    sol = Solution()
    print("Is scheduling possible: " +
          str(sol.findOrder(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))
    print("Is scheduling possible: " + str(sol.findOrder(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(sol.findOrder(3, [[0, 1], [1, 2], [2, 0]])))


main()


# Time Complexity
# In step ‘d’, each task can become a source only once and each edge (prerequisite) will be accessed and removed once. Therefore, the time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites.


# Space Complexity
# The space complexity will be O(V+E), since we are storing all of the prerequisites for each task in an adjacency list.


# Similar Problems
# Course Schedule: There are ‘N’ courses, labeled from ‘0’ to ‘N-1’. Each course has some prerequisite courses which need to be completed before it can be taken. Given the number of courses and a list of prerequisite pairs, write a method to find the best ordering of the courses that a student can take in order to finish all courses.

# Solution: This problem is exactly similar to our parent problem. In this problem, we have courses instead of tasks.
