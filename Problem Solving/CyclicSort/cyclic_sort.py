# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

# Write a function to sort the objects in-place on their creation sequence number in  without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

# Example 1:

# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]
# Example 2:

# Input: [2, 6, 4, 3, 1, 5]
# Output: [1, 2, 3, 4, 5, 6]
# Example 3:

# Input: [1, 5, 6, 4, 3, 2]
# Output: [1, 2, 3, 4, 5, 6]

# Time Complexity
# The time complexity of the above algorithm is (n). Although we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop, but in the worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move on to the next number by incrementing i. So overall, our algorithm will take O(n)+O(n-1), which is asymptotically equivalent to O(n).

# Space Complexity
# The algorithm runs in constant space O(1).



class Solution:
    def sort(self, nums):
        i = 0
        while i < len(nums):
            # Calculate the index where the current element should be placed.
            j = nums[i]-1
            # Check if the current element is not in its correct position.
            if nums[i] != nums[j]:
                # Swap the current element with the one at its correct position.
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # If the current element is already in its correct position, move to the next element.
                i += 1
        return nums

def main():
  sol = Solution()
  print(sol.sort([3, 1, 5, 4, 2]))
  print(sol.sort([2, 6, 4, 3, 1, 5]))
  print(sol.sort([1, 5, 6, 4, 3, 2]))

main()

