# Write a Recursive Approach to Split BST.

# Given a Binary Search Tree (BST) and a target value, split the BST into two subtrees where one subtree contains nodes with values less than the target value, and the other subtree contains nodes with values greater than or equal to the target value. Return the two root nodes of the resulting subtrees.

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> Tuple[Optional[TreeNode],Optional[TreeNode]]:
        if root is None:
            return None, None  # Base case: empty subtree

        if root.val <= target:
            right_split = self.splitBST(root.right, target)  # Split right subtree recursively
            root.right = right_split[0]  # Connect the resulting right subtree to the current node's right
            return root, right_split[1] # Return root and right subtree
        else:
            left_split = self.splitBST(root.left, target)  # Split left subtree recursively
            root.left = left_split[1]  # Connect the resulting left subtree to the current node's left
            return left_split[0], root  # Return left subtree and root
    
    def print_bst(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        left = self.print_bst(root.left)
        right = self.print_bst(root.right)
        return left + " " + str(root.val) + " " + right


sol = Solution()
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(7)
target1 = 5

root2 = TreeNode(3)
root2.left = TreeNode(2)
root2.right = TreeNode(4)
target2 = 4

root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)
target3 = 1

# Split BSTs
split1 = sol.splitBST(root1, target1)
split2 = sol.splitBST(root2, target2)
split3 = sol.splitBST(root3, target3)

# Print results
print("Split BST 1:", sol.print_bst(split1[0]), ",", sol.print_bst(split1[1]))
print("Split BST 2:", sol.print_bst(split2[0]), ",", sol.print_bst(split2[1]))
print("Split BST 3:", sol.print_bst(split3[0]), ",", sol.print_bst(split3[1]))
