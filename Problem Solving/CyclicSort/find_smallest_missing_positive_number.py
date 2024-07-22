# Given an unsorted array containing numbers, find the smallest missing positive number in it.

# Note: Positive numbers start from '1'.

# Example 1:

# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Example 2:

# Input: [3, -2, 0, 1, 2]
# Output: 4
# Example 3:

# Input: [3, 2, 5, 1]
# Output: 4
# Example 4:

# Input: [33, 37, 5]
# Output: 1

# This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number with one big difference. In this problem, the numbers are not bound by any range so we can have any number in the input array.

# However, we will follow a similar approach though as discussed in Find the Missing Number to place the numbers on their correct indices and ignore all numbers that are out of the range of the array (i.e., all negative numbers and all numbers greater than the length of the array). Once we are done with the cyclic sort we will iterate the array and the first index that does not have the correct number will be the smallest missing positive number!

# Tc: O(n) Sc: O(1)

class Solution:
    def findNumber(self, nums):
        i = 0
        n = len(nums)
        # Rearrange the elements to place each positive integer at its correct index.
        # Negative numbers and numbers greater than the array size are ignored.
        while i < n:
            j = nums[i]-1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        
        # Find the first index where the element does not match its expected positive value.
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        # If all elements from 1 to n are present, return n + 1.
        return len(nums)+1

def main():
    sol = Solution()
    print(sol.findNumber([-3, 1, 5, 4, 2]))
    print(sol.findNumber([3, -2, 0, 1, 2]))
    print(sol.findNumber([3, 2, 5, 1]))


main()