# Given a binary search tree (BST) and a target number, you need to find a node value in the BST that is closest to the given target. A BST is a tree where for every node, the values in the left subtree are smaller than the node, and the values in the right subtree are greater.

# Examples:

# Example 1:

# Input:

#     Tree: 
#        5
#      /   \
#     3     8
#    / \   / \
#   1   4 6   9
# Target: 6.4

# Expected Output: 6

class TreeNode:
    def __init__(self, x):
        self.val = x          # Value stored in the node.
        self.left = None      # Reference to the left child.
        self.right = None     # Reference to the right child.

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # Initialize the closest value to the root's value.
        # This acts as a running minimum difference tracker.
        closest_val = root.val
        
        while root:
            if abs(target-root.val) < abs(target - closest_val):
                closest_val = root.val
            if target < root.val:
                root = root.left # type: ignore
            else:
                root = root.right # type: ignore
        return closest_val
    
if __name__ == "__main__":
    # Constructing a sample BST for testing.
    example1 = TreeNode(5)
    example1.left = TreeNode(3) # type: ignore
    example1.left.left = TreeNode(1) # type: ignore
    example1.left.right = TreeNode(4) # type: ignore
    example1.right = TreeNode(8) # type: ignore
    example1.right.left = TreeNode(6) # type: ignore
    example1.right.right = TreeNode(9) # type: ignore
    
    solution = Solution()
    
    # Test the closestValue function with the target value 6.4.
    print(solution.closestValue(example1, 6.4))  # Expected output: 6