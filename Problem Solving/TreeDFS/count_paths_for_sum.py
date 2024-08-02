# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

# This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. But there will be four differences:

# We will keep track of the current path in a list which will be passed to every recursive call.
# Whenever we traverse a node we will do two things:
# Add the current node to the current path.
# As we added a new node to the current path, we should find the sums of all sub-paths ending at the current node. If the sum of any sub-path is equal to ‘S’ we will increment our path count.
# We will traverse all paths and will not stop processing after finding the first path.
# Remove the current node from the current path before returning from the function. This is needed to Backtrack while we are going up the recursive call stack to process other paths.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPaths(self, root, S):
        return self.count_paths_recursive(root, S, [])
    
    def count_paths_recursive(self, currNode, S, currPath):
        if currNode is None:
            return 0
        
        # add the current node to the path
        currPath.append(currNode.val)
        pathCount, pathSum = 0, 0
        # find the sums of all sub-paths in the current path list
        for i in range(len(currPath)-1, -1, -1):
            pathSum += currPath[i]
            # if the sum of any sub-path is equal to 'S' we increment our path count.
            if pathSum == S:
                pathCount += 1
        
        # traverse the left sub-tree
        pathCount += self.count_paths_recursive(currNode.left, S, currPath)
        # traverse the right sub-tree
        pathCount += self.count_paths_recursive(currNode.right, S, currPath)
        
        # remove the current node from the path to backtrack
        # we need to remove the current node while we are going up the recursive call stack
        del currPath[-1]
        return pathCount

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(sol.countPaths(root, 11)))


main()


# Time Complexity

# The time complexity of the above algorithm is O(N^2) in the worst case, where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once, but for every node, we iterate the current path. The current path, in the worst case, can be O(N) (in the case of a skewed tree). But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., O(logN). So the best case of our algorithm will be O(NlogN).

# Space Complexity

# The space complexity of the above algorithm will be O(N). This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child). We also need O(N) space for storing the currentPath in the worst case.

# Overall space complexity of our algorithm is O(N).

# ---------------------------------------------------------------------------------

# Optimised Solution

# We can consider each path as an array and calculate its prefix sums to find any required sub-paths. In the above tree, the highlighted sub-paths are exactly the same as our previous array example.

# Here is what our new algorithm will look like:

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
  def count_paths(self, root, target_sum):
      # A map that stores the number of times a prefix sum has occurred so far.
      map = {}

      return self.count_paths_prefix_sum(root, target_sum, map, 0)


  def count_paths_prefix_sum(self, current_node, target_sum, map, current_path_sum):
      if current_node is None:
          return 0

      # The number of paths that have the required sum.
      path_count = 0

      # 'current_path_sum' is the prefix sum, i.e., sum of all node values from the root 
      # to the current node.
      current_path_sum += current_node.val

      # This is the base case. If the current sum is equal to the target sum, we have found 
      # a path from root to the current node having the required sum. Hence, we increment 
      # the path count by 1.
      if target_sum == current_path_sum:
          path_count += 1

      # 'current_path_sum' is the path sum from root to the current node. If within this path, 
      # there is a valid solution, then there must be an 'old_path_sum' such that:
      # => current_path_sum - old_path_sum = target_sum
      # => current_path_sum - target_sum = old_path_sum
      # Hence, we can search such an 'old_path_sum' in the map from the key 
      # 'current_path_sum - target_sum'.
      path_count += map.get(current_path_sum - target_sum, 0)

      # This is the key step in the algorithm. We are storing the number of times the prefix sum
      # `current_path_sum` has occurred so far.
      map[current_path_sum] = map.get(current_path_sum, 0) + 1

      # Counting the number of paths from the left and right subtrees.
      path_count += self.count_paths_prefix_sum(current_node.left, target_sum, map, current_path_sum)
      path_count += self.count_paths_prefix_sum(current_node.right, target_sum, map, current_path_sum)

      # Removing the current path sum from the map for backtracking.
      # 'current_path_sum' is the prefix sum up to the current node. When we go 
      # back (i.e., backtrack), then the current node is no more a part of the path, hence, we 
      # should remove its prefix sum from the map.
      map[current_path_sum] = map.get(current_path_sum, 1) - 1

      return path_count


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(sol.count_paths(root, 11)))


main()

'''

# Time Complexity
# As we are not traversing the current path for each node, the time complexity of the above algorithm will be O(N) in the worst case, where ‘N’ is the total number of nodes in the tree.

# Space Complexity
# The space complexity of the above algorithm will be O(N). This space will be used to store the recursion stack, as well as for the prefix sum.