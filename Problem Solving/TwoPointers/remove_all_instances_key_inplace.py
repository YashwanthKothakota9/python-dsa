# Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

# Example 1:

# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

# Example 2:

# Input: [2, 11, 2, 2, 1], Key=2
# Output: 2
# Explanation: The first two elements after removing every 'Key' will be [11, 1].

# Tc: O(N) Sc: O(1)

class Solution:
    def removeKey(self, arr, key):
        
        nextElement = 0
        
        for i in range(len(arr)):
            if arr[i] != key:
                arr[nextElement] = arr[i]
                nextElement += 1
        
        return nextElement

def main():
  sol = Solution()
  
  # Test case 1
  print("Array new length: " + str(sol.removeKey([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  
  # Test case 2
  print("Array new length: " + str(sol.removeKey([2, 11, 2, 2, 1], 2)))

main()
