# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.


# This problem follows the Binary Tree Path Sum problem. We can follow the same DFS approach. There will be two differences though:

# Every time we find a root-to-leaf path, we will store it in a list. We will traverse all paths and will not stop processing after finding the first path.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPaths(self, root, required_sum):
        allPaths = []
        self.findPaths_recursive(root, required_sum, [], allPaths)
        return allPaths
    
    def findPaths_recursive(self, currNode, required_sum, currPath, allPaths):
        if currNode is None:
            return
        
        # add the current node to the path
        currPath.append(currNode.val)
        
        # if the current node is a leaf and its value is equal to required_sum, save the 
        # current path
        if currNode.val == required_sum and currNode.left is None \
            and currNode.right is None:
                allPaths.append(list(currPath))
        else:
            # traverse the left sub-tree
            self.findPaths_recursive(currNode.left, required_sum - currNode.val, currPath, allPaths)
            # traverse the right sub-tree
            self.findPaths_recursive(currNode.right, required_sum - currNode.val, currPath, allPaths)
        
        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del currPath[-1]


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(sol.findPaths(root, required_sum)))


main()

# The time complexity of the above algorithm is O(N^2), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once (which will take O(N)), and for every leaf node, we might have to store its path (by making a copy of the current path) which will take O(N).

# We can calculate a tighter time complexity of O(NlogN) from the space complexity discussion below.

# Sc: O(NlogN)

# Similar Problems
# Problem 1: Given a binary tree, return all root-to-leaf paths.

# Solution: We can follow a similar approach. We just need to remove the “check for the path sum.”

# Problem 2: Given a binary tree, find the root-to-leaf path with the maximum sum.

# Solution: We need to find the path with the maximum sum. As we traverse all paths, we can keep track of the path with the maximum sum.


