# We are given an unsorted array containing n+1 numbers taken from the range 1 to n. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

# Example 1:

# Input: [1, 4, 4, 3, 2]
# Output: 4
# Example 2:

# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
# Example 3:

# Input: [2, 4, 1, 4, 4]
# Output: 4

# This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number. Following a similar approach, we will try to place each number on its correct index. Since there is only one duplicate, if while swapping the number with its index both the numbers being swapped are same, we have found our duplicate!

# Tc: O(n) Sc: O(1)

class Solution:
    def findDuplicate(self, nums):
        i = 0
        while i < len(nums):
            # Check if the current element is in its correct position
            if nums[i] != i+1:
                # Calculate the correct index for the current element
                j = nums[i]-1
                # Check if the current element is not equal to the element at its correct index
                if nums[i] != nums[j]:
                    # Swap the elements to their correct positions
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    # We have found the duplicate
                    return nums[i]
            else:
                # Move to the next element
                i += 1
        # No duplicate found
        return -1

def main():
  sol = Solution()
  print(sol.findDuplicate([1, 4, 4, 3, 2]))
  print(sol.findDuplicate([2, 1, 3, 3, 5, 4]))
  print(sol.findDuplicate([2, 4, 1, 4, 4]))

main()

# -------------------------------------------------------------------

# Solving above problem without modifying input array

# While doing the cyclic sort, we realized that the array will have a cycle due to the duplicate number and that the start of the cycle will always point to the duplicate number. This means that we can use the fast & the slow pointer method to find the duplicate number or the start of the cycle similar to Start of LinkedList Cycle.

class Solution:
    def findDuplicate(self, arr):
        slow, fast = arr[0], arr[arr[0]]
        while slow!=fast:
            slow = arr[slow]
            fast = arr[arr[fast]]
        
        # find cycle length
        current = arr[arr[slow]]
        cycleLength = 1
        while current != arr[slow]:
            current = arr[current]
            cycleLength += 1
        
        return self.findStart(arr, cycleLength)

    def findStart(self, arr, cycleLength):
        pointer1, pointer2 = arr[0], arr[0]
        # move pointer2 ahead 'cycleLength' steps
        while cycleLength > 0:
            pointer2 = arr[pointer2]
            cycleLength -= 1
        
        # increment both pointers until they meet at the start of the cycle
        while pointer1 != pointer2:
            pointer1 = arr[pointer1]
            pointer2 = arr[pointer2]
        
        return pointer1

def main():
  sol = Solution()
  print(sol.findDuplicate([1, 4, 4, 3, 2]))
  print(sol.findDuplicate([2, 1, 3, 3, 5, 4]))
  print(sol.findDuplicate([2, 4, 1, 4, 4]))


main()
