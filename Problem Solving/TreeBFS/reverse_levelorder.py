# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only difference will be that instead of appending the current level at the end, we will append the current level at the beginning of the result list.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def traverse(self, root):
        result = deque()
        
        if root is None:
            return result
        
        q = deque()
        q.append(root)
        
        while q:
            levelSize = len(q)
            currLevel = []
            for _ in range(levelSize):
                currNode = q.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            result.appendleft(currLevel)
        
        print(result)
        result = [list(sublist) for sublist in result]
        return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(sol.traverse(root)))


main()


# Time Complexity
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space Complexity
# The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.