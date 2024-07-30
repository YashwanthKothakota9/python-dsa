# Given a non-negative integer represented as a string num and an integer k, delete k digits from num to obtain the smallest possible integer. Return this minimum possible integer as a string.

# Examples

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: The digits removed are 4, 3, and 2 forming the new number 1219 which is the smallest.
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Removing the leading 1 forms the smallest number 200.
# Input: num = "1901042", k = 4
# Output: "2"
# Explanation: Removing 1, 9, 1, and 4 forms the number 2 which is the smallest possible.

# The idea is to keep removing the peak digit from the number num. The peak digit in a number is a digit after which the next digit is smaller. By doing so, we are always trying to minimize the leftmost digit which will give us the smallest possible number.

# We can use a monotonically increasing stack to keep track of the decreasing peak digits.

# Algorithm Walkthrough

# Initialize an empty stack.
# Iterate over the digits in num.
# For each digit:
# While k is greater than 0, the stack is not empty and the current digit is smaller than the top digit on the stack, pop the top digit from the stack and decrease k by 1.
# Push the current digit onto the stack.
# If k is still greater than 0, pop k digits from the stack.
# Build the result string from the digits in the stack. Remove the leading zeros.
# If the result string is empty, return "0". Otherwise, return the result string.


class Solution:
    def removeKdigits(self, num:str, k:int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Truncate the remaining K digits
        stack = stack[:-k] if k > 0 else stack
        
        # Remove any leading zeros
        return ''.join(stack).lstrip("0") or "0"

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeKdigits("1432219", 3)) # Output: "1219"
    print(solution.removeKdigits("10200", 1)) # Output: "200"
    print(solution.removeKdigits("1901042", 4)) # Output: "2"   
    

# Time: O(N) where N is the number of digits in input.
# Space: O(N) to store stack.