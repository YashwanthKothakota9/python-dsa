# Given a binary array nums containing only 0 and 1 and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Examples
# Example 1:

# Input: nums = [1, 0, 0, 1, 1, 0, 1, 1], k = 2
# Expected Output: 6
# Justification: By flipping 0 at the second and fifth index in the list, we get [1, 0, 1, 1, 1, 1, 1, 1], which has 6 consecutive 1s.
# Example 2:

# Input: nums = [1, 0, 1, 1, 0, 0, 1, 1], k = 1
# Expected Output: 4
# Justification: By flipping 0 at 1st index, we get [1, 1, 1, 1, 0, 1, 1, 1], with a maximum of 4 consecutive 1s.
# Example 3:

# Input: nums = [1, 0, 0, 1, 1, 0, 1], k = 3
# Expected Output: 7
# Justification: By flipping all three zeros, we get [1, 1, 1, 1, 1, 1, 1], which has 7 consecutive 1s.
# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


# Solution
# To solve this problem, we'll use a sliding window approach. We'll keep a window of 1s that we expand as long as the number of 0s within the window doesn't exceed k. If the number of 0s exceeds k, we'll move the start of the window forward to reduce the number of 0s. This approach ensures that we always have the longest possible window of 1s by changing at most k 0s to 1s.

# This approach works effectively because it processes each element in the list once, ensuring that the algorithm runs in linear time. By keeping track of the count of 0s within the current window, we can dynamically adjust the window size to maximize the sequence of consecutive 1s.

# Algorithm Walkthrough
# Input: nums = [1, 0, 0, 1, 1, 0, 1, 1], k = 2

# Initialization:

# left = 0
# right = 0
# max_length = 0
# zero_count = 0
# First Iteration (right = 0):

# nums[0] is 1.
# zero_count remains 0.
# max_length is updated to 1 (window: [1]).
# Increment right to 1.
# Second Iteration (right = 1):

# nums[1] is 0.
# Increment zero_count to 1.
# max_length is updated to 2 (window: [1, 0]).
# Increment right to 2.
# Third Iteration (right = 2):

# nums[2] is 0.
# Increment zero_count to 2.
# max_length is updated to 3 (window: [1, 0, 0]).
# Increment right to 3.
# Fourth Iteration (right = 3):

# nums[3] is 1.
# zero_count remains 2.
# max_length is updated to 4 (window: [1, 0, 0, 1]).
# Increment right to 4.
# Fifth Iteration (right = 4):

# nums[4] is 1.
# zero_count remains 2.
# max_length is updated to 5 (window: [1, 0, 0, 1, 1]).
# Increment right to 5.
# Sixth Iteration (right = 5):

# nums[5] is 0.
# Increment zero_count to 3.
# zero_count exceeds k, so start adjusting left:
# nums[0] is 1, zero_count remains 3, increment left to 1.
# nums[1] is 0, decrement zero_count to 2, increment left to 2.
# max_length remains 5 (window: [0, 1, 1, 0]).
# Increment right to 6.
# Seventh Iteration (right = 6):

# nums[6] is 1.
# zero_count remains 2.
# max_length is updated to 5 (window: [0, 1, 1, 0, 1]).
# Increment right to 7.
# Eighth Iteration (right = 7):

# nums[7] is 1.
# zero_count remains 2.
# max_length is updated to 6 (window: [0, 1, 1, 0, 1, 1]).
# Increment right to 8, which ends the loop as right equals the length of nums.
# Return Result:

# The final value of max_length is 6.

# Complexity Analysis
# Time Complexity: O(n)

# The algorithm uses a sliding window approach with two pointers (left and right), which traverse the array only once. Hence, the overall time complexity is O(n), where n is the length of the array.
# Space Complexity: O(1)

# The algorithm uses a constant amount of extra space (only a few integer variables), so the space complexity is O(1).

class Solution:
    def maxConsecutiveOnes(self, nums, k):
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right-left+1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1, 1], 2))  # 6
    print(sol.maxConsecutiveOnes([1, 0, 1, 1, 0, 0, 1, 1], 1))  # 4
    print(sol.maxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1], 3))     # 7
