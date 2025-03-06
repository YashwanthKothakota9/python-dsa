# Given a nums array containing positive integers and a positive integer target, return the minimum length of a subarray having the sum of elements greater than or equal to target. If there is no such subarray, return 0 instead.

# Examples
# Example 1:

# Input: target = 15, nums = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected Output: 2
# Justification: The subarray [7, 8] has a sum of 15, which is equal to target and is the smallest possible subarray.
# Example 2:

# Input: target = 11, nums = [2, 1, 5, 2, 8]
# Expected Output: 3
# Justification: The subarray [5, 2, 8] has a sum of 15, which meets the target and is the smallest possible subarray.
# Example 3:

# Input: target = 8, nums = [2, 1, 5, 2, 3]
# Expected Output: 3
# Justification: The subarray [5, 2, 3] has a sum of 10, which meets the target and is the smallest possible subarray.

# Solution
# To solve this problem, we use a sliding window approach. This method involves maintaining a window that expands and contracts while checking the sum of its elements. By adjusting the window's size dynamically, we can efficiently find the minimum length subarray that meets or exceeds the target sum. This approach works because it avoids re-evaluating sums from scratch, reducing unnecessary calculations.

# This method is effective because it allows us to traverse the array in linear time. We expand the window by moving the right end until the sum is sufficient, then contract by moving the left end to find the smallest subarray. This two-pointer technique ensures we cover all possibilities without redundant checks, optimizing performance.

# Using Example 1:

# Input: target = 15, nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Initialize Variables:

# start = 0
# min_length = infinity
# current_sum = 0
# Iterate Through Array:

# end = 0: Add nums[0] to current_sum → current_sum = 1

# current_sum (1) is less than target (15), so do nothing.
# end = 1: Add nums[1] to current_sum → current_sum = 3

# current_sum (3) is less than target (15), so do nothing.
# end = 2: Add nums[2] to current_sum → current_sum = 6

# current_sum (6) is less than target (15), so do nothing.
# end = 3: Add nums[3] to current_sum → current_sum = 10

# current_sum (10) is less than target (15), so do nothing.
# end = 4: Add nums[4] to current_sum → current_sum = 15

# current_sum (15) is equal to target (15), so:
# Update min_length → min_length = min(infinity, 4 - 0 + 1) = 5
# Subtract nums[start] (1) from current_sum → current_sum = 14
# Increment start → start = 1
# end = 5: Add nums[5] to current_sum → current_sum = 20

# current_sum (20) is greater than target (15), so:
# Update min_length → min_length = min(5, 5 - 1 + 1) = 5
# Subtract nums[start] (2) from current_sum → current_sum = 18
# Increment start → start = 2
# current_sum (18) is still greater than target (15), so:
# Update min_length → min_length = min(5, 5 - 2 + 1) = 4
# Subtract nums[start] (3) from current_sum → current_sum = 15
# Increment start → start = 3
# current_sum (15) is equal to target (15), so:
# Update min_length → min_length = min(4, 5 - 3 + 1) = 3
# Subtract nums[start] (4) from current_sum → current_sum = 11
# Increment start → start = 4
# end = 6: Add nums[6] to current_sum → current_sum = 18

# current_sum (18) is greater than target (15), so:
# Update min_length → min_length = min(3, 6 - 4 + 1) = 3
# Subtract nums[start] (5) from current_sum → current_sum = 13
# Increment start → start = 5
# end = 7: Add nums[7] to current_sum → current_sum = 21

# current_sum (21) is greater than target (15), so:
# Update min_length → min_length = min(3, 7 - 5 + 1) = 3
# Subtract nums[start] (6) from current_sum → current_sum = 15
# Increment start → start = 6
# current_sum (15) is equal to target (15), so:
# Update min_length → min_length = min(3, 7 - 6 + 1) = 2
# Subtract nums[start] (7) from current_sum → current_sum = 8
# Increment start → start = 7
# Finalize Result:

# min_length is 2, which is not infinity.
# Return min_length, which is 2.
# This is the smallest subarray whose sum is at least 15, and it is [7, 8].

# Time Complexity: The time complexity of this algorithm is O(n), where n is the length of the array. This is because each element is processed at most twice, once by the end pointer and once by the start pointer.
# Space Complexity: The space complexity of this algorithm is O(1) because we are using a constant amount of extra space regardless of the input size.

class Solution:
    def minSubArrayLen(self, nums, target):
        min_length = float('inf')
        curr_sum = 0
        start = 0

        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_length = min(min_length, end-start+1)
                curr_sum -= nums[start]
                start += 1
        return 0 if min_length == float('inf') else min_length


sol = Solution()
print(sol.minSubArrayLen(15, [1, 2, 3, 4, 5, 6, 7, 8]))  # Output: 2
print(sol.minSubArrayLen(11, [2, 1, 5, 2, 8]))  # Output: 3
print(sol.minSubArrayLen(8, [2, 1, 5, 2, 3]))  # Output: 3
