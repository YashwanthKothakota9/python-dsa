# Given a Binary Search Tree (BST) and a range defined by two integers, L and R, calculate the sum of all the values of nodes that fall within this range. The node's value is inclusive within the range if and only if L <= node's value <= R.

# Examples:

# Example 1:

# Input:

# Tree: 
#    10
#   /  \
#  5   15
# / \   \
# 3   7   18
# Range: [7, 15]
# Expected Output: 32

# Justification: The values that fall within the range [7, 15] are 7, 10, and 15. Their sum is 7 + 10 + 15 = 32.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self,root:TreeNode,L:int,R:int)->int:
        if not root:
            return 0
        # If the current node's value is out of the range on the higher side
        if root.val > R:
            return self.rangeSumBST(root.left,L,R) # type: ignore
        # If the current node's value is out of the range on the lower side
        if root.val < L:
            return self.rangeSumBST(root.right,L,R) # type: ignore
        # Current node's value is in the range, include it and check both children
        return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R) # type: ignore
    

if __name__ == "__main__":
    # Test using the examples provided
    example1 = TreeNode(10)
    example1.left = TreeNode(5)
    example1.left.left = TreeNode(3)
    example1.left.right = TreeNode(7)
    example1.right = TreeNode(15)
    example1.right.right = TreeNode(18)

    solution = Solution()
    print(solution.rangeSumBST(example1, 7, 15))  # Expected output: 32