# Given a binary tree and an integer key, find the level order successor of the node containing the given key as a value in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only difference will be that we will not keep track of all the levels. Instead we will keep inserting child nodes to the queue. As soon as we find the given node, we will return the next node from the queue as the level order successor.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def findSuccessor(self, root, key):
        if root is None:
            return None
        q = deque()
        q.append(root)
        while q:
            currNode = q.popleft()
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
            
            if currNode.val == key:
                break
        return q[0] if q else None


def main():
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  
  result = sol.findSuccessor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = sol.findSuccessor(root, 9)
  if result:
    print(result.val)
  
  result = sol.findSuccessor(root, 12)
  if result:
    print(result.val)


main()


#  Tc: O(N) Sc: O(N)