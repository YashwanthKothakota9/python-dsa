# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator. For example, do not use pow(x, 0.5) in C++ or x ** 0.5 in Python.

# Example 1:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.8284, and since we need to return the floor of the square root (integer), hence we returned 2.  
# Example 2:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2.
# Example 3:

# Input: x = 2
# Output: 1
# Explanation: The square root of 2 is 1.414, and since we need to return the floor of the square root (integer), hence we returned 1.  

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x//2
        pivot = 0
        num = 0
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        
        return right

solution = Solution()

input1 = 4
expectedOutput1 = 2
result1 = solution.mySqrt(input1)
print(result1 == expectedOutput1) # Expected output: True

input2 = 8
expectedOutput2 = 2
result2 = solution.mySqrt(input2)
print(result2 == expectedOutput2) # Expected output: True

input4 = 2
expectedOutput4 = 1
result4 = solution.mySqrt(input4)
print(result4 == expectedOutput4) # Expected output: True

input5 = 3
expectedOutput5 = 1
result5 = solution.mySqrt(input5)
print(result5 == expectedOutput5) # Expected output: True

input6 = 15
expectedOutput6 = 3
result6 = solution.mySqrt(input6)
print(result6 == expectedOutput6) # Expected output: True
