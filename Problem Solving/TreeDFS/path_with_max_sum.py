# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.

# This problem follows the Binary Tree Path Sum pattern and shares the algorithmic logic with Tree Diameter. We can follow the same DFS approach. The only difference will be to ignore the paths with negative sums. Since we need to find the overall maximum sum, we should ignore any path which has an overall negative sum.

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMaxPathSum(self, root):
        self.globalMaxSum = -math.inf
        self.find_max_path_sum_recursive(root)
        return self.globalMaxSum
    
    def find_max_path_sum_recursive(self, currNode):
        if currNode is None:
            return 0
        
        maxPathSumFromLeft = self.find_max_path_sum_recursive(currNode.left)
        maxPathSumFromRight = self.find_max_path_sum_recursive(currNode.right)
        
        # ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        maxPathSumFromLeft = max(maxPathSumFromLeft, 0)
        maxPathSumFromRight = max(maxPathSumFromRight, 0)
        
        # maximum path sum at the current node will be equal to the sum from the left 
        # subtree + the sum from right subtree + val of current node
        localMaxSum = maxPathSumFromLeft + maxPathSumFromRight + currNode.val
        
        # update the global maximum sum
        self.globalMaxSum = max(self.globalMaxSum, localMaxSum)
        
        # maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(maxPathSumFromLeft, maxPathSumFromRight) + currNode.val


def main():
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(sol.findMaxPathSum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(sol.findMaxPathSum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(sol.findMaxPathSum(root)))


main()


# Time Complexity
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space Complexity
# The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).