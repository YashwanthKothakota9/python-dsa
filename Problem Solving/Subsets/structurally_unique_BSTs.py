# Given a number n, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to n?

# Example 1:

# Input: 2
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:

# Input: 3
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1 to 3:

# This problem follows the Subsets pattern and is quite similar to Evaluate Expression. Following a similar approach, we can iterate from 1 to ‘n’ and consider each number as the root of a tree. All smaller numbers will make up the left sub-tree and bigger numbers will make up the right sub-tree. We will make recursive calls for the left and right sub-trees


from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left:Optional[TreeNode] = None
        self.right:Optional[TreeNode] = None

class Solution:
    def findUniqueTrees(self, n):
        if n <=0:
            return []
        return self.findUnique_trees_recursive(1, n)

    def findUnique_trees_recursive(self, start, end):
        result = []
        # base condition, return 'None' for an empty sub-tree
        # consider n = 1, in this case we will have start = end = 1, this means we should have 
        # only one tree we will have two recursive calls, findUniqueTreesRecursive(1, 0) & 
        # (2, 1) both of these should return 'None' for the left and the right child
        if start > end:
            result.append(None)
            return result
        
        for i in range(start, end+1):
            # making 'i' the root of the tree
            leftSubtrees = self.findUnique_trees_recursive(start, i - 1)
            rightSubtrees = self.findUnique_trees_recursive(i + 1, end)
            for leftTree in leftSubtrees:
                for rightTree in rightSubtrees:
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    result.append(root)
        
        return result

def main():
  sol = Solution()
  print("Total trees: " + str(len(sol.findUniqueTrees(2))))
  print("Total trees: " + str(len(sol.findUniqueTrees(3))))


main()

# Tc: O(n*2^n) Sc: O(n*2^n)
# Memoized version
# Since our algorithm has overlapping subproblems, can we use memoization to improve it? We could, but every time we return the result of a subproblem from the cache, we have to clone the result list because these trees will be used as the left or right child of a tree. This cloning is equivalent to reconstructing the trees; therefore, the overall time complexity of the memoized algorithm will also be the same.