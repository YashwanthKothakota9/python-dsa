# Given an array of integers nums, return the number of operations required to make all elements in nums equal. To perform one operation, you can follow the below steps:

# Select the maximum element of nums. If there are multiple occurrences of the maximum element, choose the element which has lowest index i.
# Select the second largest element of nums.
# Replace the element at index i with the second largest element.

# Example 1:

# Input: [3, 5, 5, 2]
# Expected output: 5
# Justification:
# The largest element is 5. Reducing both 5s to 3 requires two operations.
# Update array will be [3, 3, 3, 2].
# Three more operations are needed to reduce the 3 to 2. The updated array will be [2, 2, 2, 2].
# A total five operations make all elements equal to 2.
# Example 2:

# Input: [11, 9, 7, 5, 3]
# Expected output: 10
# Justification:
# Each number needs to be reduced stepwise to the next smaller number until all are equal to the smallest number 3.
# 1 operation is required to convert 11 to 9. The updated array will be [9, 9, 7, 5, 3].
# 2 operations are required to convert 9 to 7. The updated array will be [7, 7, 7, 5, 3].
# 3 operations are required to convert 7 to 5. The updated array will be [5, 5, 5, 5, 3].
# 4 operations are required to convert 5 to 3. The updated array will be [3, 3, 3, 3, 3].
# Tota numbers of operations: 1 + 2 + 3 + 4 = 10.

# To solve this problem, the most effective approach involves sorting the array and leveraging the sorted structure to determine the reduction operations efficiently. The solution is driven by identifying and counting the number of elements that must be reduced to each unique lesser value until all elements are the same. The frequency of each distinct value in the array provides a clear path for determining the number of necessary operations.

# By sorting the array, we can work backwards, starting from the largest element, and reduce it step by step to match the next distinct element in the sorted order. This method ensures that the number of operations is minimized since we always reduce the largest elements first and in bulk, which decreases the number of total operations.

class Solution:
    def reductionOperations(self, nums):
        nums.sort()
        operations = 0
        count = 1
        for i in range(len(nums)-1,0,-1):
            # If the current number is different from the previous one
            if nums[i]!=nums[i-1]:
                # Increment the total operations by the current count
                operations += count
            # Increment the count for the next number
            count += 1
        return operations

solution = Solution()
# Test cases
print(solution.reductionOperations([3, 5, 5, 2])) # 5
print(solution.reductionOperations([11, 9, 7, 5, 3])) # 10
print(solution.reductionOperations([8, 8, 8, 8])) # 0

