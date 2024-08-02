# Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.


# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only difference will be that while traversing we will remember (irrespective of the level) the previous node to connect it with the current node.


from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.next: Optional[TreeNode] = None


class Solution:
    def connect(self, root):
        
        if root is None:
            return root
        
        q = deque()
        q.append(root)
        currNode, prevNode = None, None
        while q:
            currNode = q.popleft()
            if prevNode:
                prevNode.next = currNode
            prevNode = currNode
            
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        
        return root

def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next  

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sol.connect(root)
  print_tree(root)

main()

# Tc: O(N) Sc: O(N)

