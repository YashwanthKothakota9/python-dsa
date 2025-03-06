# Given a binary array nums, return the length of the longest non-empty subarray containing only 1's after removing 1 element from the array. Return 0 if there is no such subarray.

# Examples
# Example 1
# Input: [1, 1, 0, 0, 1, 1]
# Expected Output: 2
# Justification: By removing the first 0, you get [1, 1, 0, 1, 1] and the longest sequence of 1s is [1, 1].
# Example 2
# Input: [1, 1, 0, 1, 1, 1]
# Expected Output: 5
# Justification: By removing the first 0, you get [1, 1, 1, 1, 1] which is the longest sequence of 1s .
# Example 3
# Input: [1, 0, 1, 1, 0, 1]
# Expected Output: 3
# Justification: By removing the 0 between the first and third 1, you get [1, 1, 1, 0, 1], which has a length of 3.

# Solution
# To solve this problem, we'll use a sliding window technique to keep track of the longest segment of 1s, allowing for one 0 to be removed. We'll maintain a window defined by two pointers. If a 0 is encountered, we'll shift our window's start to the right past this 0. This approach ensures we consider every possible subarray where one 0 can be removed to get the longest segment of 1s.

# This approach is effective because it efficiently narrows down the possible subarrays without requiring nested loops, which would increase the computational complexity. Instead, by moving pointers within a single pass through the list, we achieve a linear time solution, making it optimal for larger inputs.


# Algorithm Walkthrough
# Using the example input [1, 0, 1, 1, 0, 1]:

# Initial State:

# left = 0, right = 0, zeroCount = 0, maxLen = 0
# Array: [1, 0, 1, 1, 0, 1]
# Step 1:

# Move right to 0.
# nums[right] is 1, so zeroCount remains 0.
# Current window: [1]
# maxLen = max(0, 0 - 0) = 0
# right moves to 1.
# Step 2:

# right at 1.
# nums[right] is 0, so zeroCount increments to 1.
# Current window: [1, 0]
# maxLen = max(0, 1 - 0) = 1
# right moves to 2.
# Step 3:

# right at 2.
# nums[right] is 1, so zeroCount remains 1.
# Current window: [1, 0, 1]
# maxLen = max(1, 2 - 0) = 2
# right moves to 3.
# Step 4:

# right at 3.
# nums[right] is 1, so zeroCount remains 1.
# Current window: [1, 0, 1, 1]
# maxLen = max(2, 3 - 0) = 3
# right moves to 4.
# Step 5:

# right at 4.
# nums[right] is 0, so zeroCount increments to 2.
# Since zeroCount > 1, adjust left.
# nums[left] is 1, so zeroCount remains 2.
# left moves to 1.
# nums[left] is 0, so zeroCount decrements to 1.
# left moves to 2.
# Current window: [1, 1, 0, 1]
# maxLen = max(3, 4 - 2) = 3
# right moves to 5.
# Step 6:

# right at 5.
# nums[right] is 1, so zeroCount remains 1.
# Current window: [1, 1, 0, 1]
# maxLen = max(3, 5 - 2) = 3
# right moves to 6 (end of array).
# Final State:

# The maximum length of a subarray containing only 1s after removing one element is 3.

# Complexity Analysis
# Time Complexity
# The time complexity of the solution is O(n), where n is the length of the input array nums. This is because we iterate through the array only once with the right pointer, and the left pointer also moves at most n times. Each element is processed a constant number of times, resulting in linear time complexity.

# Space Complexity
# The space complexity of the solution is O(1). This is because we use a constant amount of extra space regardless of the size of the input array


class Solution:
    def longestSubarray(self, nums) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([1, 1, 0, 0, 1, 1]))  # Output: 2
    print(sol.longestSubarray([1, 1, 0, 1, 1, 1]))  # Output: 5
    print(sol.longestSubarray([1, 0, 1, 1, 0, 1]))  # Output: 3
