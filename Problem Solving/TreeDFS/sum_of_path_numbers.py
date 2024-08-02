# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

# This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. The additional thing we need to do is to keep track of the number representing the current path.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSumOfPathNumbers(self, root):
        return self.find_root_to_leaf_path_numbers(root, 0)

    def find_root_to_leaf_path_numbers(self, currNode, pathSum):
        if currNode is None:
            return 0
        # calculate the path number of the current node
        pathSum = 10 * pathSum + currNode.val
        
        # if the current node is a leaf, return the current path sum
        if currNode.left is None and currNode.right is None:
            return pathSum
        
        # traverse the left and the right sub-tree
        return self.find_root_to_leaf_path_numbers(currNode.left, pathSum) + \
            self.find_root_to_leaf_path_numbers(currNode.right, pathSum)

def main():
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(sol.findSumOfPathNumbers(root)))


main()


# Tc: O(N) Sc: O(N)

