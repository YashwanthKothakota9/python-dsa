# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.


# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only difference will be, instead of keeping track of all the nodes in a level, we will only track the depth of the tree. As soon as we find our first leaf node, that level will represent the minimum depth of the tree.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        

class Solution:
    def findDepth(self, root):
        if root is None:
            return 0
        q = deque()
        q.append(root)
        minTreeDepth = 0
        while q:
            minTreeDepth += 1
            levelSize = len(q)
            for _ in range(levelSize):
                currNode = q.popleft()
                
                if not currNode.left and not currNode.right:
                    return minTreeDepth
                
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(sol.findDepth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(sol.findDepth(root)))


main()

# Tc: O(n) Sc: O(n)

# ----------------------------------------------------------

# Max Depth of tree (height)

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
  def find_maximum_depth(self, root):
    if root is None:
      return 0

    queue = deque()
    queue.append(root)
    maximumTreeDepth = 0
    while queue:
      maximumTreeDepth += 1
      levelSize = len(queue)
      for _ in range(levelSize):
        currentNode = queue.popleft()

        # insert the children of current node in the queue
        if currentNode.left:
          queue.append(currentNode.left)
        if currentNode.right:
          queue.append(currentNode.right)

    return maximumTreeDepth


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Maximum Depth: " + str(sol.find_maximum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Maximum Depth: " + str(sol.find_maximum_depth(root)))


main()
