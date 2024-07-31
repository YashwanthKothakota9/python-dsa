# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

# Since we need to traverse all nodes of each level before moving onto the next level, we can use the Breadth First Search (BFS) technique to solve this problem.

# We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

# Start by pushing the root node to the queue.
# Keep iterating until the queue is empty.
# In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
# Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
# After removing each node from the queue, insert both of its children into the queue.
# If the queue is not empty, repeat from step 3 for the next level.


from collections import deque
from typing import Deque, Optional, List

class TreeNode:
    def __init__(self, val:int):
        self.val:int = val
        self.left: Optional[TreeNode] = None
        self.right:Optional[TreeNode] = None

class Solution:
    def traverse(self, root:Optional[TreeNode])-> List[List[int]]:
        result:List[List[int]] = []
        
        if root is None:
            return result
        
        q:Deque[TreeNode] = deque()
        q.append(root)
        
        while q:
            levelSize = len(q)
            currentLevel = []
            for _ in range(levelSize):
                currNode:TreeNode = q.popleft()
                currentLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        
            result.append(currentLevel)
        
        return result


def main() -> None:
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(sol.traverse(root)))


main()                

# Time Complexity
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space Complexity
# The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.