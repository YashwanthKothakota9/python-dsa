class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def inorderTraversal(self, root):
        result = []
        self.inorder(root, result)
        return result
    def inorder(self, node, result):
        if node is None:
            return
        self.inorder(node.left,result)
        result.append(node.val)
        self.inorder(node.right, result)
        
root = TreeNode(1)
root.right = TreeNode(2) # type: ignore
root.right.left = TreeNode(3) # type: ignore

inorderTraversal = Solution()
result = inorderTraversal.inorderTraversal(root)

print("Inorder Traversal:", result)
