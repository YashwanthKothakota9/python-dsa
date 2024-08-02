# Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only additional thing we will be doing is to append the last node of each level to the result array.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left:Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def traverse(self, root):
        result = []
        
        if root is None:
            return result
        
        q = deque()
        q.append(root)
        while q:
            levelSize = len(q)
            for i in range(0, levelSize):
                currNode = q.popleft()
                
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                
            result.append(currNode.val)
        
        return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = sol.traverse(root)
  print("Tree right view: ")
  for val in result:
    print(str(val) + " ", end='')


main()

# Tc: O(N) Sc: O(N)

# ----------------------------------------------------------

# Problem 1: Given a binary tree, return an array containing nodes in its left view. The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.

# Solution: We will be following a similar approach, but instead of appending the last element of each level, we will be appending the first element of each level to the output array.