# Problem Statement
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

# Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

# Examples
# Example 1:

# Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
# Output: true
# Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
# Example 2:

# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: true
# Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2]
# Example 3:

# Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
# Output: false
# Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.


# Solution
# This problem is asking us to find out if it is possible to find a topological ordering of the given tasks. The tasks are equivalent to the vertices and the prerequisites are the edges.

# We can use a similar algorithm as described in Topological Sort to find the topological ordering of the tasks. If the ordering does not include all the tasks, we will conclude that some tasks have cyclic dependencies.

# Step-by-step Algorithm
# Initialize:

# Create an inDegree hashmap to keep count of incoming edges for every vertex (task).
# Create a graph hashmap to represent the adjacency list of the graph.
# Initialize both inDegree and graph for all tasks.
# Build the Graph:

# For each prerequisite pair, update the adjacency list in graph and increment the inDegree for the child task.
# Find All Sources:

# Find all vertices (tasks) with 0 in-degrees (no prerequisites) and add them to the sources queue.
# Process Each Source:

# While there are tasks in the sources queue:
# Remove a task from sources and add it to the sortedOrder.
# For each child of the current task, decrement its inDegree by 1.
# If a child's inDegree becomes 0, add it to the sources queue.
# Check for Cyclic Dependencies:

# If the sortedOrder contains all tasks, it means there are no cyclic dependencies, and all tasks can be scheduled.
# If not, there is a cyclic dependency, and the tasks cannot be scheduled.

from collections import deque


class Solution:
    def isSchedulingPossible(self, tasks, prerequisites):
        sortedOrder = []
        if tasks <= 0:
            return False

        inDegree = {i: 0 for i in range(tasks)}
        graph = {i: [] for i in range(tasks)}

        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            inDegree[child] += 1

        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        return len(sortedOrder) == tasks


def main():
    sol = Solution()
    print("Is scheduling possible: " +
          str(sol.isSchedulingPossible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))
    print("Is scheduling possible: " +
          str(sol.isSchedulingPossible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(sol.isSchedulingPossible(3, [[0, 1], [1, 2], [2, 0]])))


main()


# Time Complexity
# In step ‘d’, each task can become a source only once, and each edge (i.e., prerequisite) will be accessed and removed once. Therefore, the time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites.

# Space Complexity
# The space complexity will be O(V+E), since we are storing all of the prerequisites for each task in an adjacency list.


# Similar Problems
# Course Schedule: There are ‘N’ courses, labeled from ‘0’ to ‘N-1’. Each course can have some prerequisite courses which need to be completed before it can be taken. Given the number of courses and a list of prerequisite pairs, find if it is possible for a student to take all the courses.

# Solution: This problem is exactly similar to our parent problem. In this problem, we have courses instead of tasks.
