# Given an input array of integers nums, find an integer array, let's call it differenceArray, of the same length as an input integer array.

# Each element of differenceArray, i.e., differenceArray[i], should be calculated as follows: take the sum of all elements to the left of index i in array nums(let's call it leftSumi), and subtract it from the sum of all elements to the right of index i in array nums (let's call it rightSumi), taking the absolute value of the result:

# differenceArray[i] = | leftSumi - rightSumi |

# If there are no elements to the left or right of i, the corresponding sum should be taken as 0.
# Examples

# Example 1:

#     Input: nums = [2, 5, 1, 6, 1]
#     Expected Output: [13, 6, 0, 7, 14]
#     Explanation:
#         For i = 0: | (0) - (5+1+6+1) | = | 0 - 13 | = 13
#         For i = 1: | (2) - (1+6+1) | = | 2 - 8 | = 6
#         For i = 2: | (2+5) - (6+1) | = | 7 - 7 | = 0
#         For i = 3: | (2+5+1) - (1) | = | 8 - 1 | = 7
#         For i = 4: | (2+5+1+6) - (0) | = | 14 - 0 | = 14

# Example 2:

#     Input: nums = [3, 3, 3]
#     Expected Output: [6, 0, 6]
#     Explanation:
#         For i = 0: | (0) - (3+3) | = 6
#         For i = 1: | (3) - (3) | = 0
#         For i = 2: | (3+3) - (0) | = 6

# Example 3:

#     Input: nums = [1, 2, 3, 4, 5]
#     Expected Output: [14, 11, 6, 1, 10]
#     Explanation:
#         Calculations for each index i will follow the above-mentioned logic.

# Constraints:

#     1 <= nums.length <= 1000
#     1 <= nums[i] <= 105


# Solution

# To solve this problem, we use a two-pass approach. First, we calculate the total sum of the array. Then, we iterate through the array to compute the absolute difference between the sum of elements to the left and the sum of elements to the right for each position. This is done efficiently using two variables: leftSum to keep track of the sum of elements to the left and rightSum to keep track of the sum of elements to the right. As we traverse the array, we update these sums and calculate the differences. This ensures that the solution runs in linear time, making it efficient for large inputs.
# Step-by-step Algorithm

# Initialize variables leftSum and rightSum to 0.
#  Calculate the total sum of the array and store it in rightSum.
#   Initialize an array differenceArray to store the differences.
#    Iterate through the array nums:
#         Subtract the current element from rightSum.
#         Calculate the absolute difference between rightSum and leftSum and store it in differenceArray at the current index.
#         Add the current element to leftSum.
#     Return the differenceArray as the result.


# Time Complexity

# First loop (calculating rightSum): The first loop iterates through the entire array to calculate the total sum (rightSum). This takes O(N) time, where N is the number of elements in the array.
#  Second loop(calculating differenceArray): The second loop iterates through the array again to calculate the difference between leftSum and rightSum for each index. This also takes O(N) time.

# Since both loops run sequentially, the total time complexity is O(N+N) = O(N).

# Overall time complexity: O(N)

# Space Complexity

# Difference array: The algorithm creates an additional array differenceArray of size N to store the result. This array requires O(N) space.

# Additional variables: The algorithm uses a few extra variables(leftSum, rightSum), which require constant space, O(1).

# Overall space complexity: O(N) due to the space needed for the differenceArray.

class Solution:
    def findDifferenceArray(self, nums):
        n = len(nums)
        difference_array = [0]*n
        left_sum = 0
        right_sum = sum(nums)

        for i in range(n):
            right_sum -= nums[i]
            difference_array[i] = abs(right_sum - left_sum)
            left_sum += nums[i]

        return difference_array


solution = Solution()

example1 = [2, 5, 1, 6, 1]
example2 = [3, 3, 3]
example3 = [1, 2, 3, 4, 5]

print(solution.findDifferenceArray(example1))  # Output: [13, 6, 0, 7, 14]
print(solution.findDifferenceArray(example2))  # Output: [6, 0, 6]
print(solution.findDifferenceArray(example3))  # Output: [14, 11, 6, 1, 10]
