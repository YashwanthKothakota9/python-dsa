# Given an integer array nums, return the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

# A middleIndex is an index where the sum of the numbers to the left of this index is equal to the sum of the numbers to the right of this index.

# You can consider the left sum 0 for middleIndex == 0, and right sum 0 for middleIndex == nums.length - 1.

# If no middleIndex exists in nums, return -1.

# Examples
# Example 1:
# Input: nums = [1, 7, 3, 6, 5, 6]
# Expected Output: 3
# Justification: The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of the numbers to the right of index 3 (5 + 6 = 11).
# Example 2:
# Input: nums = [2, 1, -1]
# Expected Output: 0
# Justification: The sum of the numbers to the left of index 0 is considered to be 0. The sum of the numbers to the right of index 0 (1 + -1 = 0) is also 0.
# Example 3:
# Input: nums = [2, 3, 5, 5, 3, 2]
# Expected Output: -1
# Justification: There is no middleIndex exists in the array.

# To solve this problem, we need to find an index where the sum of the elements on the left equals the sum of the elements on the right. We can achieve this by calculating the total sum of the array first. Then, as we iterate through the array, we keep a running sum of the elements to the left of the current index. By subtracting this running sum and the current element from the total sum, we get the sum of the elements to the right of the current index. If the left sum equals the right sum at any index, we return that index. This approach ensures that we only need to traverse the array once, making it efficient in terms of time complexity.

# This method is effective because it minimizes the number of passes over the array, reducing the overall time complexity to O(n). Additionally, it only requires a few extra variables for storing sums, keeping the space complexity to O(1). This combination of efficiency and simplicity makes it a robust solution for finding the middle index.

# Step-by-step Algorithm
# Calculate the total sum of the array.
# Initialize a variable leftSum to 0.
# Iterate through the array using a loop:
# For each element at index i, calculate the right sum as totalSum - leftSum - nums[i].
# If leftSum equals the right sum, return i.
# Update leftSum by adding the current element nums[i].
# If no index is found, return -1.
# Algorithm Walkthrough
# Let's walk through the algorithm using the example nums = [1, 7, 3, 6, 5, 6].

# Step 1: Calculate totalSum = 1 + 7 + 3 + 6 + 5 + 6 = 28.
# Step 2: Initialize leftSum = 0.
# Step 3: Start loop through the array.
# Index 0: rightSum = 28 - 0 - 1 = 27. leftSum = 0 + 1 = 1.
# Index 1: rightSum = 28 - 1 - 7 = 20. leftSum = 1 + 7 = 8.
# Index 2: rightSum = 28 - 8 - 3 = 17. leftSum = 8 + 3 = 11.
# Index 3: rightSum = 28 - 11 - 6 = 11.
# leftSum equals rightSum at index 3. Return 3.


class Solution:
    def findMiddleIndex(self, nums) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1


solution = Solution()
example1 = [1, 7, 3, 6, 5, 6]
example2 = [2, 1, -1]
example3 = [2, 3, 5, 5, 3, 2]
print(solution.findMiddleIndex(example1))  # Output: 3
print(solution.findMiddleIndex(example2))  # Output: 0
print(solution.findMiddleIndex(example3))  # Output: -1


# Time Complexity: O(n)
# We traverse the array twice, once to calculate the total sum and once to find the middle index.
# Space Complexity: O(1)
# We use a constant amount of extra space for variables (totalSum, leftSum).
