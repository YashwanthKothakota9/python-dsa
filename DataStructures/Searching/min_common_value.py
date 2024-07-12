# Given two sorted arrays nums1 and nums2 containing integers only, return the smallest integer that appears in both arrays. If there isn't any integer that exists in both arrays, the function should return -1.

# Examples
# Example 1:

# input: nums1 = [1, 3, 5, 7], nums2 = [3, 4, 5, 6, 8, 10]
# expectedOutput: 3
# Justification: Both arrays share the integers 3 and 5, but the smallest common integer is 3.
# Example 2:

# input: nums1 = [2, 4, 6], nums2 = [1, 3, 5]
# expectedOutput: -1
# Justification: There are no integers common to both nums1 and nums2, hence the output is -1.
# Example 3:

# input: nums1 = [1, 2, 2, 3], nums2 = [2, 2, 4]
# expectedOutput: 2
# Justification: The integer 2 is the only common number between nums1 and nums2, appearing multiple times in both, and it is the smallest.

class Solution:
    def findMinimumCommonValue(self, nums1, nums2):
        # Ensure binary search is done on the larger array
        if len(nums1) > len(nums2):
            return self.findMinimumCommonValue(nums2, nums1)
        
        # Search for each element of the smaller array in the larger array
        for num in nums1:
            if self.binarySearch(nums2, num):
                return num  # Return the common element found
        
        # If no common elements are found, return -1
        return -1

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        # Continue searching while left pointer is less than or equal to right pointer
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index
            if nums[mid] > target:
                right = mid - 1  # If target is less than element at mid, search left half
            elif nums[mid] < target:
                left = mid + 1  # If target is greater than element at mid, search right half
            else:
                return True  # Target found
        return False  # Target not found

solution = Solution()
# Test cases
print(solution.findMinimumCommonValue([1, 3, 5, 7], [3, 4, 5, 6, 8, 10]))  # Expected Output: 3
print(solution.findMinimumCommonValue([2, 4, 6], [1, 3, 5]))  # Expected Output: -1
print(solution.findMinimumCommonValue([1, 2, 2, 3], [2, 2, 4]))  # Expected Output: 2

    