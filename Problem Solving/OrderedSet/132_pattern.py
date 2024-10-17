# Given an array nums, containing N integers.

# A 132 pattern consists of three numbers, say x, y, and z, where x < z and z < y. This is often referred to as a '132' pattern because if we represent x, y, and z as 1, 3, and 2, respectively, it mimics the positional pattern in '132'.

# Return true if such a pattern exists within any sequence of given numbers nums. Otherwise, return false.

# Examples
# Example 1:

# Input: nums = [3, 5, 0, 3, 4]
# Expected Output: True
# Justification: Here, 3 < 4 and 4 < 5, forming a '132' pattern with the numbers 3, 5, and 4.
# Example 2:

# Input: nums = [1, 2, 3, 4]
# Expected Output: False
# Justification: The sequence is in ascending order, and no '132' pattern is present.
# Example 3:

# Input: nums = [9, 11, 8, 9, 10, 7, 9]
# Expected Output: True
# Justification: The pattern is formed with 8 < 9 and 9 < 10 in sequence 8, 10, 9.

# The 132 Pattern problem requires finding a sequence of three numbers in an array such that the first number is smaller than the third number, which is in turn smaller than the second number. In other words, for indices i, j, and k, we need to find a pattern where nums[i] < nums[k] < nums[j] with i < j < k.

# To solve this problem efficiently, we use a combination of a stack and a set to track potential candidates for the 132 pattern as we iterate through the array from the end to the beginning. This approach ensures that we can quickly identify and verify the necessary conditions for the pattern.

# Step-by-Step Algorithm
# Initialize Data Structures:

# Create a SortedSet named second to store potential candidates for the second number in the 132 pattern.
# Create a stack named st to manage the numbers during the traversal.
# Iterate Through the Array from End to Beginning:

# Loop through the array from the last element to the first element (i.e., from right to left).
# Manage the Stack:

# For each element nums[i] in the array:
# While the stack is not empty and the top element of the stack is smaller than nums[i], pop the element from the stack and add it to the second set.
# Check for the 132 Pattern:

# If the stack is not empty and the second set is not empty:
# Iterate through the second set to find the smallest number that is greater than nums[i]. This is done using the higher method of SortedSet which finds the smallest number in the set that is greater than nums[i].
# If such a number is found, it confirms the presence of the 132 pattern, and we return True.
# Push the Current Number onto the Stack:

# Push the current number nums[i] onto the stack to potentially serve as the second number in future iterations.
# End of Iteration:

# If the loop completes without finding a 132 pattern, return False.


# Algorithm Walkthrough
# Using the input nums = [9, 11, 8, 9, 10, 7, 9]:

# Initialize Data Structures:

# second = {} (empty set)
# st = [] (empty stack)
# Iteration from End to Beginning:

# i = 6 (nums[i] = 9):

# Stack is empty.
# Push 9 onto the stack: st = [9].
# i = 5 (nums[i] = 7):

# Stack contains 9, which is greater than 7.
# Push 7 onto the stack: st = [9, 7].
# i = 4 (nums[i] = 10):

# Pop elements from the stack while they are smaller than 10:
# Pop 7, insert into second: second = {7}, st = [9].
# Pop 9, insert into second: second = {7, 9}, st = [].
# Stack is empty.
# Push 10 onto the stack: st = [10].
# i = 3 (nums[i] = 9):

# Stack contains 10, which is greater than 9.
# Check second for an element greater than 9:
# second.upper_bound(9) finds 9, which is not greater than 9, so continue.
# Push 9 onto the stack: st = [10, 9].
# i = 2 (nums[i] = 8):

# Stack contains 9, which is greater than 8.
# Check second for an element greater than 8:
# second.upper_bound(8) finds 9, which is greater than 8.
# A 132 pattern is found with 8 < 9 and 9 < 10.
# Return True.


import bisect


class Solution:
    def find132pattern(self, nums):
        second = []  # List to store potential candidates for the second number
        st = []  # Stack to manage the numbers

        # Iterate through the array from the end to the beginning
        for i in range(len(nums)-1, -1, -1):
            # Pop elements from the stack that are smaller than the current number
            while st and st[-1] < nums[i]:
                second.append(st.pop())

            # Check if the current number can be part of a 132 pattern
            if st and second:
                # Find the position of the smallest number in the list greater than nums[i]
                pos = bisect.bisect_right(second, nums[i])
                if pos < len(second):
                    return True  # If such a number exists, we found a 132 pattern

            # Push the current number onto the stack
            st.append(nums[i])
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.find132pattern([3, 5, 0, 3, 4]))  # Output: True
    print(sol.find132pattern([1, 2, 3, 4]))  # Output: False
    print(sol.find132pattern([9, 11, 8, 9, 10, 7, 9]))  # Output: True

# Complexity Analysis
# Time Complexity: The time complexity is O(nlogn) due to the use of the SortedSet to find the higher bound, which takes O(logn) time for each insertion and query. The overall complexity is O(nlogn) since we iterate through the list once and perform log-time operations on the set.
# Space Complexity: The space complexity is O(n) for the stack and set, which can store up to (n) elements in the worst case.


# Solution Using Stack
# To solve this problem, we need to find a sequence of numbers in the array that follows the pattern 132. Specifically, we need to find indices i, j, and k such that i < j < k and nums[i] < nums[k] < nums[j].

# We can achieve this by iterating backward through the array, using a stack to keep track of potential values for nums[k]. By maintaining a variable z to represent the largest value we have found that is smaller than the current number, we can efficiently check for the 132 pattern.

# Step-by-Step Algorithm
# Initialization:

# Initialize z to Integer.MIN_VALUE to represent the largest value smaller than the current number.
# Create an empty stack to keep track of potential values for nums[k].
# Iterate Backward:

# Loop through the array nums from the end to the beginning.
# Check for Pattern:

# For each nums[i], check if it is less than z. If true, return True since we have found a 132 pattern.
# Update z and Stack:

# While the stack is not empty and the top of the stack is less than nums[i], update z to the top value of the stack and pop the stack.
# Push the current nums[i] onto the stack.
# Return Result:

# If the loop completes without finding the pattern, return False.
# Algorithm Walkthrough
# Using the input: [9, 11, 8, 9, 10, 7, 9]

# Initialization:

# z = Integer.MIN_VALUE
# stack = []
# Iterate Backward:

# Start from the last element and move to the first.
# Iteration Details:

# Step 1: nums[6] = 9
# Stack is empty, push 9 onto the stack.
# stack = [9]
# Step 2: nums[5] = 7
# 7 is not less than z (which is Integer.MIN_VALUE).
# Push 7 onto the stack.
# stack = [9, 7]
# Step 3: nums[4] = 10
# 10 is not less than z.
# While stack top is less than 10, update z and pop from the stack.
# z = 7, stack = [9]
# z = 9, stack = []
# Push 10 onto the stack.
# stack = [10]
# Step 4: nums[3] = 9
# 9 is not less than z (which is 9).
# While stack top is less than 9, update z and pop from the stack.
# z = 9, stack = [10]
# Push 9 onto the stack.
# stack = [10, 9]
# Step 5: nums[2] = 8
# 8 is less than z(9). So, return true. .

class Solution2:
    def find132Pattern(self, nums):
        z = float('-inf')  # Initialize z to the smallest possible value
        set_nums = []

        for num in reversed(nums):  # Iterate backwards through the list
            if num < z:
                return True
            while set_nums and set_nums[-1] < num:
                z = set_nums.pop()  # Update z to the largest smaller element
            set_nums.append(num)  # Add the current number to the set

        return False


if __name__ == "__main__":
    solution = Solution2()
    print(solution.find132Pattern([3, 5, 0, 3, 4]))  # True
    print(solution.find132Pattern([1, 2, 3, 4]))  # False
    print(solution.find132Pattern([9, 11, 8, 9, 10, 7, 9]))  # True


# Complexity Analysis
# Time Complexity
# Building the stack: Each element is pushed onto the stack exactly once and can be popped from the stack at most once. Therefore, the operations of pushing and popping elements are O(1) each.
# Overall: Since we iterate through the array exactly once and perform O(1) operations for each element (push and pop from the stack), the total time complexity is O(n), where n is the number of elements in the array.
# Space Complexity
# Stack Space: In the worst case, all elements are pushed onto the stack, leading to a stack space usage of O(n).
# Variable Space: The additional space used by the variable z is O(1).
# Overall: The overall space complexity is O(n), due to the space used by the stack.
