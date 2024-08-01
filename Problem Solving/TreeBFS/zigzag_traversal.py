# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.


# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only additional step we have to keep in mind is to alternate the level order traversal, which means that for every other level, we will traverse similar to Reverse Level Order Traversal.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def traverse(self, root):
        result = []
        if root is None:
            return result
        
        q = deque()
        q.append(root)
        leftToRight = True
        
        while q:
            levelSize = len(q)
            currLevel = deque()
            for _ in range(levelSize):
                currNode = q.popleft()
                if leftToRight:
                    currLevel.append(currNode.val)
                else:
                    currLevel.appendleft(currNode.val)
                
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            result.append(list(currLevel))
            leftToRight = not leftToRight
        
        return result


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(sol.traverse(root)))


main()


# Time Complexity
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space Complexity
# The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.