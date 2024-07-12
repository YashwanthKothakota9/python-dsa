# Given an array nums sorted in increasing order, return the maximum between the count of positive integers and the count of negative integers.

# Note: 0 is neither positive nor negative.

# Examples
# Example 1:

# Input: nums = [-4, -3, -1, 0, 1, 3, 5, 7]
# Expected Output: 4
# Justification: The array contains three negative integers (-4, -3, -1) and four positive integers (1, 3, 5, 7). The maximum count between negatives and positives is 4.
# Example 2:

# Input: nums = [-8, -7, -5, -4, 0, 0, 0]
# Expected Output: 4
# Justification: Here, there are four negative integers (-8, -7, -5, -4) and no positives. Thus, the maximum count is 4.
# Example 3:

# Input: nums = [0, 2, 2, 3, 3, 3, 4]
# Expected Output: 6
# Justification: This input array includes zero negative integers and six positives (2, 2, 3, 3, 3, 4). Hence, the maximum count is 6.

class Solution:
    def maxCount(self, nums):
        start, end = 0, len(nums)-1
        maxNegatives, maxPositives = 0, 0
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < 0:
                maxNegatives = mid+1
                start = mid + 1
            else:
                end = mid -1
        
        start, end  = 0, len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] > 0:
                maxPositives = len(nums) - mid
                end = mid - 1
            else:
                start = mid + 1
        
        return max(maxPositives, maxNegatives)
    
solution = Solution()

# Example 1
nums1 = [-4, -3, -1, 0, 1, 3, 5, 7]
print("Example 1:", solution.maxCount(nums1))  # Expected Output: 4

# Example 2
nums2 = [-8, -7, -5, -4, 0, 0, 0]
print("Example 2:", solution.maxCount(nums2))  # Expected Output: 4

# Example 3
nums3 = [0, 2, 2, 3, 3, 3, 4]
print("Example 3:", solution.maxCount(nums3))  # Expected Output: 6