# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

# Example 1:

# Input: [4, 6, 10], key = 6
# Output: 1
# Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
# Example 2:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: 4
# Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
# Example 3:

# Input: [4, 6, 10], key = 17
# Output: -1
# Explanation: There is no number greater than or equal to '17' in the given array.
# Example 4:

# Input: [4, 6, 10], key = -1
# Output: 0
# Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.


# This problem follows the Binary Search pattern. Since Binary Search helps us find a number in a sorted array efficiently, we can use a modified version of the Binary Search to find the ceiling of a number.

# We can use a similar approach as discussed in Order-agnostic Binary Search. We will try to search for the ‘key’ in the given array. If we find the ‘key’, we return its index as the ceiling. If we can’t find the ‘key’, the next big number will be pointed out by the index start.

# Since we are always adjusting our range to find the ‘key’, when we exit the loop, the start of our range will point to the smallest number greater than the ‘key’ as shown in the above picture.

# We can add a check in the beginning to see if the ‘key’ is bigger than the biggest number in the input array. If so, we can return ‘-1’.

from typing import List

class Solution:
    def searchCeilingOfANumber(self, arr: List[int], key:int):
        n = len(arr)
        if key > arr[n-1]:
            return -1
        
        start, end = 0, n-1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1
            elif key > arr[mid]:
                start = mid + 1
            else:
                return mid
        
        # since the loop is running until 'start <= end', so at the end of the while loop, 
        # 'start == end+1' we are not able to find the element in the given array, so the next
        # big number will be arr[start]
        return start

def main():
  sol = Solution()
  print(sol.searchCeilingOfANumber([4, 6, 10], 6))
  print(sol.searchCeilingOfANumber([1, 3, 8, 10, 15], 12))
  print(sol.searchCeilingOfANumber([4, 6, 10], 17))
  print(sol.searchCeilingOfANumber([4, 6, 10], -1))


main()


# Time Complexity
# Since we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.

# Space Complexity
# The algorithm runs in constant space O(1).