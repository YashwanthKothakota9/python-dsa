# Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’

# Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.

# Example 1:

# Input: [4, 6, 10], key = 6
# Output: 1
# Explanation: The biggest number smaller than or equal to '6' is '6' having index '1'.
# Example 2:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: 3
# Explanation: The biggest number smaller than or equal to '12' is '10' having index '3'.
# Example 3:

# Input: [4, 6, 10], key = 17
# Output: 2
# Explanation: The biggest number smaller than or equal to '17' is '10' having index '2'.
# Example 4:

# Input: [4, 6, 10], key = -1
# Output: -1
# Explanation: There is no number smaller than or equal to '-1' in the given array.


class Solution:
  def searchFloorOfANumber(self, arr, key):
    if key < arr[0]:  # if the 'key' is smaller than the smallest element
      return -1

    start, end = 0, len(arr) - 1
    while start <= end:
      mid = start + (end - start) // 2
      if key < arr[mid]:
        end = mid - 1
      elif key > arr[mid]:
        start = mid + 1
      else:  # found the key
        return mid

    # since the loop is running until 'start <= end', so at the end of the while loop, 
    # 'start == end+1' we are not able to find the element in the given array, so the next 
    # smaller number will be arr[end]
    return end


def main():
  sol = Solution()
  print(sol.searchFloorOfANumber([4, 6, 10], 6))
  print(sol.searchFloorOfANumber([1, 3, 8, 10, 15], 12))
  print(sol.searchFloorOfANumber([4, 6, 10], 17))
  print(sol.searchFloorOfANumber([4, 6, 10], -1))


main()
