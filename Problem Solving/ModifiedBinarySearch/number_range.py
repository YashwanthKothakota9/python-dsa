# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

# Example 1:

# Input: [4, 6, 6, 6, 9], key = 6
# Output: [1, 3]
# Example 2:

# Input: [1, 3, 8, 10, 15], key = 10
# Output: [3, 3]
# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: [-1, -1]

# The problem follows the Binary Search pattern. Since Binary Search helps us find a number in a sorted array efficiently, we can use a modified version of the Binary Search to find the first and the last position of a number.

# We can use a similar approach as discussed in Order-agnostic Binary Search. We will try to search for the ‘key’ in the given array; if the ‘key’ is found (i.e.key == arr[middle]) we have two options:

# When trying to find the first position of the ‘key’, we can update end = middle - 1 to see if the key is present before middle.
# When trying to find the last position of the ‘key’, we can update start = middle + 1 to see if the key is present after middle.
# In both cases, we will keep track of the last position where we found the ‘key’. These positions will be the required range.

from typing import List

class Solution:
    def findRange(self, arr:List[int], key:int):
        result = [-1, -1]
        result[0] = self.binary_search(arr, key, False)
        if result[0] != -1:
            result[1] = self.binary_search(arr, key, True)
        return result
    
    def binary_search(self, arr, key, findMaxIndex):
        keyIndex = -1
        start, end = 0, len(arr)-1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1
            elif key > arr[mid]:
                start = mid + 1
            else:
                keyIndex = mid
                if findMaxIndex:
                    start = mid + 1
                else:
                    end = mid - 1
        return keyIndex

def main():
  sol = Solution()
  print(sol.findRange([4, 6, 6, 6, 9], 6))
  print(sol.findRange([1, 3, 8, 10, 15], 10))
  print(sol.findRange([1, 3, 8, 10, 15], 12))


main()


# Time Complexity
# Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.

# Space Complexity
# The algorithm runs in constant space O(1).

