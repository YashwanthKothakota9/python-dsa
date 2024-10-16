# You are given a 2D array heights[][] of size n x m, where heights[n][m] represents the height of the cell (n, m).

# Find a path from the top-left corner to the bottom-right corner that minimizes the effort required to travel between consecutive points, where effort is defined as the absolute difference in height between two points. In a single step, you can either move up, down, left or right.

# Return the minimum effort required for any path from the first point to the last.

# Example 1:

# Input: heights =
#  [[1,2,3],
#   [3,8,4],
#   [5,3,5]]
# Expected Output: 1
# Justification: The path with the minimum effort is along the edges of the grid (right, right, down, down) which requires an effort of 1 between each pair of points.
# Example 2:

# Input: heights =
# [[1,2,2],
#  [3,3,3],
#  [5,3,1]]
# Expected Output: 2
# Justification: The path that minimizes the maximum effort goes through (1,2,2,3,1), which has a maximum effort of 2 (from 3 to 1).
# Example 3:

# Input: heights =
# [[1,1,1],
#  [1,1,1],
#  [1,1,1]]
# Expected Output: 0
# Justification: The path that minimizes the maximum effort goes through (1,1,1,1,1), which has a maximum effort of 0.

# To solve this problem, we'll employ the Union Find algorithm. The core idea here is to sort all the edges (the differences in elevation between adjacent cells) in ascending order. Then, starting from the smallest edge, we'll progressively unite adjacent cells in the grid. The process of uniting cells involves linking together cells that can be reached with the current maximum effort level. This step is crucial because it helps to build a path incrementally while ensuring that we keep the effort as low as possible.

# We continue this process of uniting cells until the top-left cell and the bottom-right cell are connected. At this point, the current maximum effort level represents the minimum effort needed to traverse from the start to the end. This method efficiently finds the path with the least resistance while considering all possible paths and their associated efforts.

# The algorithm involves the following steps:

# Step 1: Initialization
# Create a UnionFind instance for a 3x3 grid, resulting in 9 elements (0 to 8).
# Initialize an empty list to store edges.
# Step 2: Building Edges
# Iterate over each cell in the grid.
# For each cell, calculate the absolute difference in elevation with its right and bottom neighbors (if they exist).
# Step 3: Sorting Edges
# Sort the edges by their elevation difference in ascending order.
# Step 4: Perform Union-Find Operations
# For each edge in the sorted list, perform the following:
# Extract the two cells (cell1 and cell2) and their elevation difference from the edge.
# Perform the union operation on cell1 and cell2.
# Step 5: Union Operation
# In the union function, find the roots of both cell1 and cell2 using the find method.
# If the roots are different, join the two sets. If one set has a higher rank (depth), make it the parent of the other.
# If both sets have equal rank, make one the parent of the other and increase the rank of the parent.
# Step 6: Find Operation
# In the find method, for a given cell, find the root of the set to which it belongs.
# Implement path compression: Set each cell along the way to point directly to the root. This optimizes future find operations.
# Step 7: Check for Connection
# After each union operation, check if the start cell and the end cell are connected.
# This is done by checking if the roots of cell 0 and cell 8 (in the UnionFind structure) are the same.
# If they are connected, stop the process.
# Step 8: Result
# The elevation difference of the last processed edge that connected the start and end cells is the minimum effort required.
# Algorithm Walkthrough
# Step 1: Initialization
# Initialize a UnionFind instance for a 3x3 grid, resulting in 9 elements.
# Create an empty list to store the edges.
# Step 2: Building Edges
# Iterate through each cell in the grid and calculate the absolute differences with its right and bottom neighbors (if they exist).
# For the input [[1,2,3],[3,8,4],[5,3,5]], create edges with their differences:
# Between (0,0) and (0,1): |1-2| = 1
# Between (0,1) and (0,2): |2-3| = 1
# Between (0,0) and (1,0): |1-3| = 2
# Between (1,0) and (2,0): |3-5| = 2
# Between (1,0) and (1,1): |3-8| = 5
# Between (1,1) and (1,2): |8-4| = 4
# Between (0,1) and (1,1): |2-8| = 6
# Between (1,1) and (2,1): |8-3| = 5
# Between (0,2) and (1,2): |3-4| = 1
# Between (1,2) and (2,2): |4-5| = 1
# Between (2,0) and (2,1): |5-3| = 2
# Between (2,1) and (2,2): |3-5| = 2
# Step 3: Union-Find Operations
# First, we sort the edges by their differences:

# Edges with Difference = 1:

# (0,0) and (0,1): Difference = 1
# (0,1) and (0,2): Difference = 1
# (0,2) and (1,2): Difference = 1
# (1,2) and (2,2): Difference = 1
# Edges with Difference = 2:

# (0,0) and (1,0): Difference = 2
# (1,0) and (2,0): Difference = 2
# (2,0) and (2,1): Difference = 2
# (2,1) and (2,2): Difference = 2
# Edges with Higher Differences (not initially relevant for the desired path).

# Now, let's perform the Union-Find operations:

# Processing Edges with Difference = 1
# Union (0,0) and (0,1):
# Connects cells 0 and 1. Parents: [0, 0, 2, 3, 4, 5, 6, 7, 8].
# Union (0,1) and (0,2):
# Connects cells 1 and 2 (and hence 0 with 2). Parents: [0, 0, 0, 3, 4, 5, 6, 7, 8].
# Union (0,2) and (1,2):
# Connects cells 2 and 5. Parents: [0, 0, 0, 3, 4, 0, 6, 7, 8].
# Union (1,2) and (2,2):
# Connects cells 5 and 8. Parents: [0, 0, 0, 3, 4, 0, 6, 7, 0].
# At this step, cells 0 and 8 are connected.
# The last edge difference is 1.

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]  # Initialize parent array
        self.rank = [0] * size  # Initialize rank array

    def find(self, x):
        # Path compression: If x is not its own parent, find its root parent.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)  # Find root parent of x
        rootY = self.find(y)  # Find root parent of y
        if rootX != rootY:  # Union the sets if they have different root parents
            # Union by rank: Attach the shorter tree to the taller one
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:  # If ranks are equal, choose any root to be the new parent and increase rank
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def minimumEffortPath(self, heights):
        row, col = len(heights), len(heights[0])
        uf = UnionFind(row * col)  # Initialize Union-Find data structure
        edges = []

        for i in range(row):
            for j in range(col):
                if i > 0:  # Add edge to the cell above (if it exists)
                    edges.append((i * col + j, (i - 1) * col + j,
                                 abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:  # Add edge to the cell on the left (if it exists)
                    edges.append((i * col + j, i * col + (j - 1),
                                 abs(heights[i][j] - heights[i][j - 1])))

        # Sort edges by the difference in heights
        edges.sort(key=lambda x: x[2])

        for x, y, diff in edges:  # Iterate through sorted edges
            uf.union(x, y)  # Union the cells connected by the edge
            # If the source and destination cells are connected, return the effort
            if uf.find(0) == uf.find(row * col - 1):
                return diff

        return 0


sol = Solution()
print("Example 1:", sol.minimumEffortPath(
    [[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # Expected Output: 1
print("Example 2:", sol.minimumEffortPath(
    [[1, 2, 2], [3, 3, 3], [5, 3, 1]]))  # Expected Output: 2
print("Example 3:", sol.minimumEffortPath(
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # Expected Output: 0


# Time Complexity
# Initialization:

# Initializing the parent and rank arrays takes O(M*N) time, where (M) is the number of rows and (N) is the number of columns.
# Creating Edges:

# Creating the edges involves iterating through each cell in the grid, resulting in O(M*N) time. Each cell potentially contributes up to two edges.
# Sorting Edges:

# Sorting the edges takes O(ElogE) time, where (E) is the number of edges. Since each cell can have up to 2 edges (except boundary cells), (E) is approximately O(2*M*N), so the sorting time complexity is O(M*N*log(M*N)).
# Union-Find Operations:

# Each union and find operation has an amortized time complexity of O(alpha(N)), where alpha(N) is the inverse Ackermann function, which is nearly constant.
# In the worst case, we perform union and find operations for each edge, resulting in O(E*alpha(M*N)). Here, (E) is approximately 2*M*N, the union-find operations take O((M*N)alpha(M*N)).
# Combining these steps, the overall time complexity is dominated by the sorting step, making it O((M*N)log(M*N)).

# Space Complexity
# The space complexity is O(M*N) for the parent and rank arrays and the edges list.
