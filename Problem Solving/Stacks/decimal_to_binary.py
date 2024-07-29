# Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

# Examples
# Example 1:

# Input: 2
# Output: "10"
# Explanation: The binary equivalent of 2 is 10.
# Example 2:

# Input: 7
# Output: "111"

class Solution:
    def decimalToBinary(self, num):
        stack = []
        while num > 0:
            stack.append(num % 2)
            num //= 2
        return ''.join(str(i) for i in reversed(stack))

sol = Solution()
print(sol.decimalToBinary(2))    # Output: "10" (Binary representation of 2)
print(sol.decimalToBinary(7))    # Output: "111" (Binary representation of 7)
print(sol.decimalToBinary(18))   # Output: "10010" (Binary representation of 18)


# The time complexity of this algorithm is O(logn) due to the division by 2 at each step.

# The space complexity is also O(logn) because in each step we will be pushing an element on the stack, and there are a total of logn steps.