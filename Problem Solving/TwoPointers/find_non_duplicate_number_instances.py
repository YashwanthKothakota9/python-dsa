# Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The non-duplicate numbers should be sorted and you should not use any extra space so that the solution has constant space complexity i.e.,O(1) .

# Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after moving element will be [2, 3, 6, 9].

# Example 2:
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after moving elements will be [2, 11].

# In this problem, we need to separate the duplicate elements in-place such that the resultant length of the array remains sorted. As the input array is sorted, one way to do this is to shift the elements left whenever we encounter duplicates. In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number. So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.

# Tc: O(n) Sc: O(1)

from typing import List


class Solution:
    def moveElements(self, arr:List[int]):
        next_non_duplicate = 1
        i = 0
        while i < len(arr):
            if arr[next_non_duplicate - 1] != arr[i]:
                arr[next_non_duplicate] = arr[i]
                next_non_duplicate += 1
            i+=1
        return next_non_duplicate
    
def main():
  # Create an instance of the Solution class
  sol = Solution()

  # Test the 'moveElements' method with example arrays
  print(sol.moveElements([2, 3, 3, 3, 6, 9, 9]))  # Output: 4 (modified array: [2, 3, 6, 9, 6, 9, 9])
  print(sol.moveElements([2, 2, 2, 11]))         # Output: 2 (modified array: [2, 11, 2, 11])

# Execute the main function
main()