# You are given an array nums containing n integers, where nums[i] represents the maximum length of a forward jump you can make from index i. You are initially positioned at nums[0].

# Return the minimum number of jumps needed to reach from the start to the end of the array.

# Examples
# Example 1:
# Input: nums = [2, 3, 2, 2, 1]
# Expected Output: 2
# Justification: Start at index 0 and jump to index 1 (jump size 1). Then, jump from index 1 to the end (jump size 3).
# Example 2:
# Input: nums = [1, 2, 3, 4, 5]
# Expected Output: 3
# Justification: Start at index 0, jump to index 1 (jump size 1). Then, jump to index 3 (jump size 2). Finally, jump to the end (jump size 2).
# Example 3:
# Input: nums = [2, 3, 1, 2, 4, 1]
# Expected Output: 3
# Justification: Start at index 0, jump to index 1 (jump size 1). Then, jump to index 4 (jump size 2). Finally, jump to the end (jump size 1).
# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

# Algorithm Walkthrough
# Using the input nums = [2, 3, 1, 2, 4, 1].

# Initialization:

# jumps = 0
# currentEnd = 0
# farthest = 0
# Iteration 1:

# Index i = 0
# farthest = max(0, 0 + 2) = 2
# Since i == currentEnd (0 == 0):
# jumps++ (jumps = 1)
# currentEnd = farthest (currentEnd = 2)
# Iteration 2:

# Index i = 1
# farthest = max(2, 1 + 3) = 4
# i != currentEnd (1 != 2), so do nothing
# Iteration 3:

# Index i = 2
# farthest = max(4, 2 + 1) = 4
# Since i == currentEnd (2 == 2):
# jumps++ (jumps = 2)
# currentEnd = farthest (currentEnd = 4)
# Iteration 4:

# Index i = 3
# farthest = max(4, 3 + 2) = 5
# i != currentEnd (3 != 4), so do nothing
# Iteration 5:

# Index i = 4
# farthest = max(5, 4 + 4) = 8
# Since i == currentEnd (4 == 4):
# jumps++ (jumps = 3)
# currentEnd = farthest (currentEnd = 8)
# Return Result:

# Return jumps which is 3.


# Complexity Analysis
# Time Complexity: The algorithm runs in O(n) time, where n is the length of the array. This is because we iterate through the array once, and each operation inside the loop (like updating the farthest point) takes constant time.
# Space Complexity: The algorithm uses O(1) additional space since we are only using a few extra variables (jumps, currentEnd, and farthest) regardless of the input size.


class Solution:
    def jump(self, nums):
        jumps = 0  # To count the number of jumps
        current_end = 0  # To mark the end of the range for the current jump
        farthest = 0  # To mark the farthest point that can be reached

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])  # Update the farthest point
            if i == current_end:  # If reached the end of the current jump range
                jumps += 1  # Increment jump count
                current_end = farthest  # Update the end of the range to the farthest point

        return jumps  # Return the number of jumps


if __name__ == "__main__":
    solution = Solution()

    # Test examples
    example1 = [2, 3, 2, 2, 1]
    example2 = [1, 2, 3, 4, 5]
    example3 = [2, 3, 1, 2, 4, 1]

    # Print the results
    print(solution.jump(example1))  # Expected Output: 2
    print(solution.jump(example2))  # Expected Output: 3
    print(solution.jump(example3))  # Expected Output: 3
