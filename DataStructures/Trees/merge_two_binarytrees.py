class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Tc: O(min(n,m)) Sc: O(min(n,m))
class Solution:
    def mergeTrees(self,t1:TreeNode,t2:TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        new_node = TreeNode(t1.val + t2.val)
        new_node.left = self.mergeTrees(t1.left,t2.left) # type: ignore
        new_node.right = self.mergeTrees(t1.right,t2.right) # type: ignore

        return new_node
    
    def print_in_order(self,node: TreeNode):
        """Utility function to print tree using inorder traversal."""
        if not node:
            return
        self.print_in_order(node.left) # type: ignore
        print(node.val, end=" ")
        self.print_in_order(node.right) # type: ignore


if __name__ == "__main__":
    # Test the algorithm with the provided input
    solution = Solution()

    tree1 = TreeNode(1)
    tree1.left = TreeNode(2) # type: ignore
    tree1.right = TreeNode(3) # type: ignore
    tree1.left.left = TreeNode(4) # type: ignore
    tree1.left.right = TreeNode(5) # type: ignore

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2) # type: ignore
    tree2.right = TreeNode(3) # type: ignore
    tree2.left.right = TreeNode(5) # type: ignore

    merged_tree = solution.mergeTrees(tree1, tree2)

    # Print the merged tree using inorder traversal
    solution.print_in_order(merged_tree)
    print()  # for a newline after traversal
