# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

# Example 1:

# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
# Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
# Example 2:

# Input: L1=[5, 8, 9], L2=[1, 7]
# Output: [1, 5, 7, 8, 9]
# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


# A brute force solution could be to add all elements of the given ‘K’ lists to one list and sort it. If there are a total of ‘N’ elements in all the input lists, then the brute force solution will have a time complexity of O(NlogN) as we will need to sort the merged list. Can we do better than this? How can we utilize the fact that the input lists are individually sorted?

# If we have to find the smallest element of all the input lists, we have to compare only the smallest (i.e. the first) element of all the lists. Once we have the smallest element, we can put it in the merged list. Following a similar pattern, we can then find the next smallest element of all the lists to add it to the merged list.

# The best data structure that comes to mind to find the smallest number among a set of ‘K’ numbers is a Heap. Let’s see how can we use a heap to find a better algorithm.

# We can insert the first element of each array in a Min Heap.

# After this, we can take out the smallest (top) element from the heap and add it to the merged list.

# After removing the smallest element from the heap, we can insert the next element of the same list into the heap.

# We can repeat steps 2 and 3 to populate the merged list in sorted order.

from heapq import *


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

  # used for the min-heap
  def __lt__(self, other):
    return self.val < other.val


class Solution:
  def merge(self, lists):
    minHeap = []

    # put the root of each list in the min heap
    for root in lists:
      if root is not None:
        heappush(minHeap, root)

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    resultHead, resultTail = None, None
    while minHeap:
      node = heappop(minHeap)
      if resultHead is None:
        resultHead = resultTail = node
      else:
        resultTail.next = node #type:ignore
        resultTail = resultTail.next#type:ignore

      if node.next is not None:
        heappush(minHeap, node.next)

    return resultHead


def main():
  sol = Solution()
  l1 = Node(2)
  l1.next = Node(6)#type:ignore
  l1.next.next = Node(8)#type:ignore

  l2 = Node(3)
  l2.next = Node(6)#type:ignore
  l2.next.next = Node(7)#type:ignore

  l3 = Node(1)
  l3.next = Node(3)#type:ignore
  l3.next.next = Node(4)#type:ignore

  result = sol.merge([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.val) + " ", end='')
    result = result.next


main()


# Time Complexity
# Since we’ll be going through all the elements of all lists and will be removing/adding one element to the heap in each step, the time complexity of the above algorithm will be O(N*logK), where ‘N’ is the total number of elements in all the ‘K’ input lists.

# Space Complexity
# The space complexity will be O(K) because, at any time, our min-heap will be storing one number from all the ‘K’ input lists.