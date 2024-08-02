# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

# This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach and additionally, track the element of the given sequence that we should match with the current node. Also, we can return false as soon as we find a mismatch between the sequence and the node value.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPath(self, root, sequence):
        if not root:
            return len(sequence) == 0
        return self.find_path_recursive(root, sequence, 0)
    
    def find_path_recursive(self, currNode, sequence, sequenceIndex):
        if currNode is None:
            return False
        
        seqLen = len(sequence)
        if sequenceIndex >= seqLen or currNode.val != sequence[sequenceIndex]:
            return False
        
        # if the current node is a leaf, add it is the end of the sequence, we have found 
        # a path!
        if currNode.left is None and currNode.right is None and \
            sequenceIndex == seqLen - 1:
                return True
        
        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.find_path_recursive(currNode.left, sequence, sequenceIndex+1) \
            or self.find_path_recursive(currNode.right, sequence, sequenceIndex + 1)

def main():
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(sol.findPath(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(sol.findPath(root, [1, 1, 6])))


main()

# Tc: O(N) Sc: O(N)

