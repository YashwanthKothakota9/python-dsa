# Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.


# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only difference is that while traversing a level we will remember the previous node to connect it with the current node.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.next: Optional[TreeNode] = None

def print_level_order(root):
    nextLevelRoot = root
    while nextLevelRoot:
        curr = nextLevelRoot
        nextLevelRoot = None
        while curr:
            print(str(curr.val)+ " ", end='')
            if not nextLevelRoot:
                if curr.left:
                    nextLevelRoot = curr.left
                elif curr.right:
                    nextLevelRoot = curr.right
            curr = curr.next
        print()

class Solution:
  def connect(self, root):
    if root is None:
      return

    queue = deque()
    queue.append(root)
    while queue:
      previousNode = None
      levelSize = len(queue)
      # connect all nodes of this level
      for _ in range(levelSize):
        currentNode = queue.popleft()
        if previousNode:
          previousNode.next = currentNode
        previousNode = currentNode

        # insert the children of current node in the queue
        if currentNode.left:
          queue.append(currentNode.left)
        if currentNode.right:
          queue.append(currentNode.right)
    return root  


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root = sol.connect(root)

  print("Level order traversal using 'next' pointer: ")
  print_level_order(root)


main()


# Tc: O(N) Sc: O(n)