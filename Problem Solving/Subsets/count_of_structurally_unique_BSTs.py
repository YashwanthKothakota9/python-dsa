# Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

# Example 1:

# Input: 2
# Output: 2
# Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.
# Example 2:

# Input: 3
# Output: 5
# Explanation: There will be 5 unique BSTs that can store numbers from 1 to 3.


# This problem is similar to Structurally Unique Binary Search Trees. Following a similar approach, we can iterate from 1 to ‘n’ and consider each number as the root of a tree and make two recursive calls to count the number of left and right sub-trees.


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution:
  def countTrees(self, n):
    if n <= 1:
      return 1
    count = 0
    for i in range(1, n+1):
      # making 'i' root of the tree
      countOfLeftSubtrees = self.countTrees(i - 1)
      countOfRightSubtrees = self.countTrees(n - i)
      count += (countOfLeftSubtrees * countOfRightSubtrees)

    return count


def main():
  sol = Solution()
  print("Total trees: " + str(sol.countTrees(2)))
  print("Total trees: " + str(sol.countTrees(3)))


main()

# Tc: O(N*2^n) Sc:O(2^n)

# Memoized version
# Our algorithm has overlapping subproblems as our recursive call will be evaluating the same sub-expression multiple times. To resolve this, we can use memoization and store the intermediate results in a HashMap. In each function call, we can check our map to see if we have already evaluated this sub-expression before. Here is the memoized version of our algorithm:


# class TreeNode:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


class Solution2:
  def countTrees(self, n):
    return self.count_trees_rec({}, n)


  def count_trees_rec(self, map, n):
    if n in map:
      return map[n]

    if n <= 1:
      return 1
    count = 0
    for i in range(1, n+1):
      # making 'i' the root of the tree
      countOfLeftSubtrees = self.count_trees_rec(map, i - 1)
      countOfRightSubtrees = self.count_trees_rec(map, n - i)
      count += (countOfLeftSubtrees * countOfRightSubtrees)

    map[n] = count
    return count


def main2():
  sol = Solution2()
  print("Total trees: " + str(sol.countTrees(2)))
  print("Total trees: " + str(sol.countTrees(3)))


main2()



# The time complexity of the memoized algorithm will be O(n^2), since we are iterating from ‘1’ to ‘n’ and ensuring that each sub-problem is evaluated only once. The space complexity will be O(n) for the memoization map.