# Given a binary tree, populate an array to represent the averages of all of its levels.


# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only difference will be that instead of keeping track of all nodes of a level, we will only track the running sum of the values of all nodes in each level. In the end, we will append the average of the current level to the result array.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def findLevelAvgs(self, root):
        result = []
        
        if root is None:
            return result

        q = deque()
        q.append(root)
        
        while q:
            levelSize = len(q)
            levelSum = 0.0
            for _ in range(levelSize):
                currNode = q.popleft()
                levelSum += currNode.val
                
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            result.append(levelSum / levelSize)

        return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(sol.findLevelAvgs(root)))


main()

# TC: O(N) Sc:O(N)


# Similar Problems
# Problem 1: Find the largest value on each level of a binary tree.

# Solution: We will follow a similar approach, but instead of having a running sum we will track the maximum value of each level.

# maxValue = max(maxValue, currentNode.val)