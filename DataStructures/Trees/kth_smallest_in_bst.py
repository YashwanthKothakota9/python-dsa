class TreeNode:
    def __init__(self, x):
        self.val = x       # Value of the node.
        self.left = None   # Reference to the left child.
        self.right = None  # Reference to the right child.

class Solution:
    def __init__(self):
        # `count` keeps track of the number of nodes we've traversed in-order.
        self.count = 0
        
        # `result` will hold our final answer.
        self.result = 0
    
    # This method is the public API that finds the kth smallest element in a BST.
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Start the in-order traversal.
        self.traverse(root, k)
        
        # Once traversal is done, the `result` will hold our answer.
        return self.result

    # A recursive function to do an in-order traversal of the BST.
    # We stop traversing once we've visited `k` nodes.
    def traverse(self, node: TreeNode, k: int):
        # If the current node is null or we've already traversed k nodes, return.
        if not node or self.count >= k:
            return
        
        # First, traverse the left subtree.
        self.traverse(node.left, k) # type: ignore
        
        # Increment the counter for the current node.
        self.count += 1
        
        # If we've traversed exactly k nodes, this is our result.
        if self.count == k:
            self.result = node.val
        
        # Finally, traverse the right subtree.
        self.traverse(node.right, k) # type: ignore

if __name__ == '__main__':
    # Constructing the tree for testing.
    example1 = TreeNode(8)
    example1.left = TreeNode(3) # type: ignore
    example1.left.left = TreeNode(1) # type: ignore
    example1.left.right = TreeNode(6) # type: ignore
    example1.left.right.left = TreeNode(4) # type: ignore
    example1.left.right.right = TreeNode(7) # type: ignore
    example1.right = TreeNode(10) # type: ignore
    example1.right.right = TreeNode(14) # type: ignore
    example1.right.right.left = TreeNode(13) # type: ignore

    solution = Solution()
    # Test the kthSmallest method.
    print(solution.kthSmallest(example1, 4))  # Expected output: 6
