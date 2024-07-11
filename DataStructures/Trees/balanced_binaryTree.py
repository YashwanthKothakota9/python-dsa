class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, node):
        if not node:
            return 0
        leftDepth = self.depth(node.left)
        if leftDepth == -1:
            return -1
        rightDepth = self.depth(node.right)
        if rightDepth == -1:
            return -1
        if abs(leftDepth - rightDepth) > 1:
            return -1
        return 1+max(leftDepth,rightDepth)
    
    def isBalanced(self,root):
        return self.depth(root) != -1
    
if __name__ == "__main__":
    # Test example 1
    example1 = TreeNode(3)
    example1.left = TreeNode(9)
    example1.right = TreeNode(20)
    example1.right.left = TreeNode(15)
    example1.right.right = TreeNode(7)

    # Test example 2
    example2 = TreeNode(1)
    example2.left = TreeNode(2)
    example2.left.left = TreeNode(3)
    example2.left.left.left = TreeNode(4)
    example2.right = TreeNode(5)

    solution = Solution()
    print(solution.isBalanced(example1))  # Expected output: true
    print(solution.isBalanced(example2))  # Expected output: false
