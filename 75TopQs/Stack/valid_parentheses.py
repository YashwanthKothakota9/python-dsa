# Problem Statement
# Determine if an input string containing only the characters '(', ')', '{', '}', '[', and ']' is valid. A string is considered valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Each close bracket has a corresponding open bracket of the same type.
# Examples
# Input: "(]"
# Expected Output: false
# Justification: The opening parenthesis '(' is not closed by its corresponding closing parenthesis.
# Input: "{[]}"
# Expected Output: true
# Justification: The string contains pairs of opening and closing brackets in the correct order.
# Input: "[{]}"
# Expected Output: false
# Justification: The opening square bracket '[' is closed by a curly brace '}', which is incorrect.

# Solution
# Initialization:
# Start with an empty stack.
# For every bracket in the input string:
# If the bracket is an opening bracket ('(', '{', '['), push it onto the stack.
# If the bracket is a closing bracket (')', '}', ']'):
# If the stack is empty, return false.
# Pop the top of the stack and check if it matches the corresponding opening bracket.
# Validation:
# If the current closing bracket doesn't match the top of the stack, return false.
# If the stack is not empty after processing all brackets in the string, return false.
# Final Output:
# If the stack is empty at the end, return true, indicating that the string has valid parentheses.

# Complexity Analysis
# Time Complexity: O(n) where n is the length of the string. Each character is processed once.
# Space Complexity: O(n) in the worst case when all characters are opening brackets.


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


solution = Solution()
print(solution.is_valid("(]"))  # false
print(solution.is_valid("{[]}"))  # true
print(solution.is_valid("[{]}"))  # false
