# Problem Statement
# Given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation (RPN), evaluate the expression and return the resulting integer value.

# The valid operators are '+', '-', '*', and '/'.
# Each operand can be an integer or another expression.
# Division between two integers should truncate towards zero.
# No division by zero will occur.
# The input is a valid RPN expression.
# All results fit within a 32-bit integer.
# Examples
# Example 1
# Input: tokens = ["2", "11", "5", "/", "+"]
# Output: 4
# Explanation: (11 / 5) = 2, then (2 + 2) = 4.
# Example 2
# Input: tokens = ["2", "3", "11", "+", "*"]
# Output: 28
# Explanation: (11 + 3) = 14, then (2 * 14) = 28.
# Example 3
# Input: tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
# Output: 14
# Explanation: (1 + 2) = 3, (3 * 4) = 12, (5 + 12) = 17, (17 - 3) = 14.
# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
# Solution
# To solve this problem, we use a stack to evaluate the Reverse Polish Notation. In RPN, every operator follows all of its operands. We process each token in the input array one by one. When we encounter an operand (number), we push it onto the stack. When we encounter an operator, we pop the required number of operands from the stack, perform the operation, and push the result back onto the stack. This approach ensures that operations are performed in the correct order. Using a stack is efficient here because it allows us to handle the nested structure of the expression naturally.

# This approach is effective because it takes advantage of the LIFO (Last In, First Out) nature of stacks, ensuring that each operation uses the most recently encountered operands. It also handles all types of valid RPN expressions without needing to parse or rearrange the input, making it straightforward and reliable.

# Time Complexity
# The time complexity of the algorithm is O(n), where n is the number of tokens in the input array. Each token is processed once, and basic stack operations (push and pop) take constant time, O(1).

# Space Complexity
# The space complexity of the algorithm is O(n), where n is the number of tokens. In the worst case, all tokens are numbers, and we push each onto the stack, resulting in a maximum stack size of n.


class Solution:
    def eval_RPN(self, tokens):
        stack = []

        for token in tokens:
            if self.is_operator(token):
                b = stack.pop()
                a = stack.pop()
                stack.append(self.apply_operator(a, b, token))
            else:
                stack.append(int(token))
        return stack.pop()

    def is_operator(self, token):
        return token == "+" or token == "-" or token == "*" or token == "/"

    def apply_operator(self, a, b, operator):
        if operator == "+":
            return a+b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return int(a / b)
        else:
            raise ValueError("Invalid operator")

    def main(self):
        sol = Solution()
        print(sol.eval_RPN(["2", "11", "5", "/", "+"]))  # 4
        print(sol.eval_RPN(["2", "3", "11", "+", "*"]))  # 28
        print(sol.eval_RPN(
            ["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # 14


if __name__ == "__main__":
    Solution().main()
