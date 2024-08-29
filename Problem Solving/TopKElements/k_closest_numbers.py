# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

# Example 1:

# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]
# Example 2:

# Input: [2, 4, 5, 6, 9], K = 3, X = 6
# Output: [4, 5, 6]
# Example 3:

# Input: [2, 4, 5, 6, 9], K = 3, X = 10
# Output: [5, 6, 9]


# This problem follows the Top ‘K’ Numbers pattern. The biggest difference in this problem is that we need to find the closest (to ‘X’) numbers compared to finding the overall largest numbers. Another difference is that the given array is sorted.

# Utilizing a similar approach, we can find the numbers closest to ‘X’ through the following algorithm:

# Since the array is sorted, we can first find the number closest to ‘X’ through Binary Search. Let’s say that number is ‘Y’.
# The ‘K’ closest numbers to ‘Y’ will be adjacent to ‘Y’ in the array. We can search in both directions of ‘Y’ to find the closest numbers.
# We can use a heap to efficiently search for the closest numbers. We will take ‘K’ numbers in both directions of ‘Y’ and push them in a Min Heap sorted by their absolute difference from ‘X’. This will ensure that the numbers with the smallest difference from ‘X’ (i.e., closest to ‘X’) can be extracted easily from the Min Heap.
# Finally, we will extract the top ‘K’ numbers from the Min Heap to find the required numbers.


from heapq import *

class Solution:
    def findClosestElements(self, arr, K, X):
        index = self.binary_search(arr, X)
        low, high = index - K, index + K
        
        # 'low' should not be less than zero
        # 'high' should not be greater the size of the array
        low = max(low, 0)
        high = min(high, len(arr)-1)
        
        minHeap = []
        # add all candidate elements to the min heap, sorted by their absolute difference 
        # from 'X'
        for i in range(low, high+1):
            heappush(minHeap, (abs(arr[i]-X), arr[i]))
        
        # we need the top 'K' elements having smallest difference from 'X'
        result = []
        for _ in range(K):
            result.append(heappop(minHeap)[1])
        
        result.sort()
        return result
    
    def binary_search(self, arr, target):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > 0:
            return low - 1
        return low

def main():
  sol = Solution()
  print("'K' closest numbers to 'X' are: " +
        str(sol.findClosestElements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(sol.findClosestElements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(sol.findClosestElements([2, 4, 5, 6, 9], 3, 10)))


main()


# Time Complexity
# The time complexity of the above algorithm is O(logN+K∗logK). We need O(logN) for Binary Search and O(K∗logK) to insert the numbers in the Min Heap, as well as to sort the output array.

# Space Complexity
# The space complexity will be O(K), as we need to put a maximum of 2K numbers in the heap.

