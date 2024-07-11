# Given a Binary Search Tree (BST), you are required to find the smallest difference between the values of any two different nodes.

# In a BST, the nodes are arranged in a manner where the value of nodes on the left is less than or equal to the root, and the value of nodes on the right is greater than the root.

# Input:
#     4
#    / \
#   2   6
#  / \
# 1   3
# Expected Output: 1
# Justification: The pairs (1,2), (2,3), or (3,4) have the smallest difference of 1.
# Example 2:

# Input:
#     10
#    /  \
#   5   15
#  / \    \
# 2   7    18
# Expected Output: 2
# Justification: The pair (5,7) has the smallest difference of 2.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # List to hold the values in order.
        self.nodes = []
    
    def inorderTraversal(self, node):
        """Helper function to perform the in-order traversal."""
        if not node:
            return
        self.inorderTraversal(node.left)   # Recursively visit the left subtree.
        self.nodes.append(node.val)        # Add the current node's value to the list.
        self.inorderTraversal(node.right)  # Recursively visit the right subtree.

    def minDiffInBst(self,root):
        self.nodes.clear()
        self.inorderTraversal(root)
        minDiff = float('inf')
        for i in range(1, len(self.nodes)):
            minDiff = min(minDiff, self.nodes[i] - self.nodes[i-1])
        return minDiff
    
if __name__ == "__main__":
    # First test case
    example1 = TreeNode(4)
    example1.left = TreeNode(2)
    example1.left.left = TreeNode(1)
    example1.left.right = TreeNode(3)
    example1.right = TreeNode(6)

    # Second test case
    example2 = TreeNode(40)
    example2.right = TreeNode(70)
    example2.right.left = TreeNode(50)
    example2.right.right = TreeNode(90)

    solution = Solution()

    print(solution.minDiffInBst(example1))  # Expected output: 1
    print(solution.minDiffInBst(example2))  # Expected output: 10 (50-40)
