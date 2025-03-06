# You are given an array of integers nums. You start at the first index of the array and each element in nums represents the maximum number of steps you can jump forward from that position.

# Return true if you can reach the last index, or false otherwise.

# Examples
# Example 1
# Input: nums = [1, 2, 3, 4, 5]
# Expected Output: true
# Justification: Starting at index 0, you can jump 1 step to index 1. From index 1, you can jump 2 steps to index 3. From index 3, you can jump 1 steps to the last index (4). Therefore, it is possible to reach the end.
# Example 2
# Input: nums = [2, 0, 2, 0, 1]
# Expected Output: true
# Justification: Starting at index 0, you can jump 2 steps to index 2. From index 2, you can jump 2 steps to the last index (4). Therefore, it is possible to reach the end.
# Example 3
# Input: nums = [1, 0, 1, 0]
# Expected Output: false
# Justification: Starting at index 0, you can jump 1 step to index 1. However, index 1 has a value of 0, which means you cannot move forward from there. Therefore, it is impossible to reach the end.
# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Step-by-Step Algorithm
# Initialize a variable maxReach to 0. This will keep track of the farthest index we can reach.
# Loop through each index i of the array nums:
# If i exceeds maxReach, return false (since we can't move beyond maxReach).
# Update maxReach to the maximum of maxReach and i + nums[i].
# If the loop completes, return true (since we can reach or exceed the last index).

# Algorithm Walkthrough
# Let's walk through the algorithm using the input [2, 0, 2, 0, 1]:

# Initialize maxReach to 0.
# At index 0:
# nums[0] is 2.
# Check if 0 > maxReach (0). This is false.
# Update maxReach to max(0, 0 + 2) = 2.
# At index 1:
# nums[1] is 0.
# Check if 1 > maxReach (2). This is false.
# maxReach remains 2 since max(2, 1 + 0) = 2.
# At index 2:
# nums[2] is 2.
# Check if 2 > maxReach (2). This is false.
# Update maxReach to max(2, 2 + 2) = 4.
# At index 3:
# nums[3] is 0.
# Check if 3 > maxReach (4). This is false.
# maxReach remains 4 since max(4, 3 + 0) = 4.
# At index 4:
# nums[4] is 1.
# Check if 4 > maxReach (4). This is false.
# Update maxReach to max(4, 4 + 1) = 5.
# Since maxReach is greater than or equal to the last index (4), we return true.

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the array nums. We only traverse the array once.
# Space Complexity: O(1). We only use a single variable maxReach to store the maximum reachable index, which requires constant space.

class Solution:
    def canJump(self, nums):
        # Initialize the maximum reachable index
        maxReach = 0
        for i in range(len(nums)):
            # If the current index is greater than max_reach, return False
            if i > maxReach:
                return False
            # Update the maximum reachable index
            maxReach = max(maxReach, i+nums[i])
        return True


if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(sol.canJump([1, 2, 3, 4, 5]))  # true
    # Example 2
    print(sol.canJump([2, 0, 2, 0, 1]))  # true
    # Example 3
    print(sol.canJump([1, 0, 1, 0]))  # false
