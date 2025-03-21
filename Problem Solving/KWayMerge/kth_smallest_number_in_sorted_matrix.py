# Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

# Example 1:

# Input: Matrix=[
#     [2, 6, 8], 
#     [3, 7, 10],
#     [5, 8, 11]
#   ], 
#   K=5
# Output: 7
# Explanation: The 5th smallest number in the matrix is 7.


# This problem follows the K-way merge pattern and can be easily converted to Kth Smallest Number in M Sorted Lists. As each row (or column) of the given matrix can be seen as a sorted list, we essentially need to find the Kth smallest number in ‘N’ sorted lists.


from heapq import *
from typing import List

class Solution:
    def findKthSmallest(self, matrix:List[List[int]], k:int):
        minHeap = []
        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for i in range(min(k,len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
        # take the smallest(top) element form the min heap, if the running count is equal to
        # 'k' return the number. If the row of the top element has more elements, add the 
        # next element to the heap
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i+1:
                heappush(minHeap, (row[i+1], i+1, row))
        return number


def main():
  sol = Solution()
  print("Kth smallest number is: " +
        str(sol.findKthSmallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()



# Time Complexity
# First, we inserted at most ‘K’ or one element from each of the ‘N’ rows, which will take O(min(K,N)). Then we went through at most ‘K’ elements in the matrix and remove/add one element in the heap in each step. As we can’t have more than ‘N’ elements in the heap in any condition, therefore, the overall time complexity of the above algorithm will be O(min(K, N) + K*logN).

# Space Complexity
# The space complexity will be O(N) because, in the worst case, our min-heap will be storing one number from each of the ‘N’ rows.


# An Alternate Approach
# Since each row and column of the matrix is sorted, is it possible to use Binary Search to find the Kth smallest number?

# The biggest problem to use Binary Search, in this case, is that we don’t have a straightforward sorted array, instead, instead, we have a matrix! As we remember, in Binary Search, we calculate the middle index of the search space (‘1’ to ‘N’) and see if our required number is pointed out by the middle index; if not we either search in the lower half or the upper half. In a sorted matrix, we can’t really find a middle. Even if we do consider some index as middle, it is not straightforward to find the search space containing numbers bigger or smaller than the number pointed out by the middle index.

# An alternative could be to apply the Binary Search on the “number range” instead of the “index range”. As we know that the smallest number of our matrix is at the top left corner and the biggest number is at the bottom right corner. These two numbers can represent the “range” i.e., the start and the end for the Binary Search. Here is how our algorithm will work:

# Start the Binary Search with start = matrix[0][0] and end = matrix[n-1][n-1].
# Find middle of the start and the end. This middle number is NOT necessarily an element in the matrix.
# Count all the numbers smaller than or equal to middle in the matrix. As the matrix is sorted, we can do this in O(N).
# While counting, we can keep track of the “smallest number greater than the middle” (let’s call it n1) and at the same time the “biggest number less than or equal to the middle” (let’s call it n2). These two numbers will be used to adjust the “number range” for the Binary Search in the next iteration.
# If the count is equal to ‘K’, n2 will be our required number as it is the “biggest number less than or equal to the middle”, and is definitely present in the matrix.
# If the count is less than ‘K’, we can update start = n2 to search in the higher part of the matrix and if the count is greater than ‘K’, we can update end = n1 to search in the lower part of the matrix in the next iteration.


class Solution2:
  def findKthSmallest(self, matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
      mid = start + (end - start) / 2
      smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

      count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger)

      if count == k:
        return smaller
      if count < k:
        start = larger  # search higher
      else:
        end = smaller  # search lower

    return start
  

  def count_less_equal(self, matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
      if matrix[row][col] > mid:
        # as matrix[row][col] is bigger than the mid, let's keep track of the
        # smallest number greater than the mid
        larger = min(larger, matrix[row][col])
        row -= 1
      else:
        # as matrix[row][col] is less than or equal to the mid, let's keep track of the
        # biggest number less than or equal to the mid
        smaller = max(smaller, matrix[row][col])
        count += row + 1
        col += 1

    return count, smaller, larger


def main2():
  sol = Solution2()
  print("Kth smallest number is: " +
        str(sol.findKthSmallest([[1, 4], [2, 5]], 2)))

  print("Kth smallest number is: " +
        str(sol.findKthSmallest([[-5]], 1)))

  print("Kth smallest number is: " +
        str(sol.findKthSmallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

  print("Kth smallest number is: " +
        str(sol.findKthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main2()


# Time Complexity
# The Binary Search could take (log(max−min)) iterations where ‘max’ is the largest and ‘min’ is the smallest element in the matrix and in each iteration we take O(N) for counting, therefore, the overall time complexity of the algorithm will be O(N*log(max-min)).

# Space Complexity
# The algorithm runs in constant space O(1).