# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example 1:

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
# Example 3:

# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted
# Example 4:

# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

# Algorithm Walkthrough
# Using the input [1, 3, 2, 0, -1, 7, 10]:

# Initialize Pointers: low = 0, high = 6.
# Find Left Boundary:
# Compare 1 and 3, move low to 1.
# Compare 3 and 2, stop. low = 1.
# Find Right Boundary:
# Compare 10 and 7, move high to 5.
# Compare 7 and -1, move high to 4.
# Compare -1 and 0, stop at 4.
# Find Min and Max:
# Subarray is [3, 2, 0, -1].
# Minimum is -1, Maximum is 3.
# Extend Left Boundary:
# 1 is greater than -1, low stays 1.
# Extend Right Boundary:
# 7 is not less than 3, high stays 4.
# Calculate Length:
# Length is high - low + 1 = 4 - 0 + 1 = 5.

# TC: O(N)
# SC: O(1)

import math


class Solution:
    def sort(self, arr):
        low, high = 0, len(arr)-1
        # find the first number out of sorting order from the beginnin
        while low < len(arr)-1 and arr[low] <= arr[low+1]:
            low += 1
        # if the array is sorted
        if low == len(arr)-1:
            return 0
        # find the first number out of sorting order from the end
        while high > 0 and arr[high] >= arr[high-1]:
            high -= 1
        # find the maximum and minimum of the subarray
        subarray_max = -math.inf
        subarray_min = math.inf
        for k in range(low, high+1):
            subarray_max = max(subarray_max, arr[k])
            subarray_min = min(subarray_min, arr[k])
        # extend the subarray to include any number which is bigger than the minimum of
    # the subarray
        while low > 0 and arr[low-1] > subarray_min:
            low -= 1
        # extend the subarray to include any number which is smaller than the maximum of
    # the subarray
        while high < len(arr)-1 and arr[high+1] < subarray_max:
            high += 1
        return [high-low+1, low, high]


def main():
    sol = Solution()
    print(sol.sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(sol.sort([1, 3, 2, 0, -1, 7, 10]))
    print(sol.sort([1, 2, 3]))
    print(sol.sort([3, 2, 1]))


main()
