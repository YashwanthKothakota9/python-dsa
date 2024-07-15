class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        
        if value < root.val:
            root.left = self.insert(root.left, value)
        elif value > root.val:
            root.right = self.insert(root.right, value)
        
        return root

def printBST(node):
    if not node:
        return
    printBST(node.left)
    print(node.val, end = " ")
    printBST(node.right)
    
root = TreeNode(4)
root.left = TreeNode(2) # type: ignore
root.right = TreeNode(7) # type: ignore
root.left.left = TreeNode(1) # type: ignore
root.left.right = TreeNode(3) # type: ignore

values = [5, 4, 2]

bstInsertion = Solution()

# Insert nodes into the BST
for value in values:
    root = bstInsertion.insert(root, value)

# Print the updated BST
print("BST After Insertion:")
printBST(root)
