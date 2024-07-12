# We can follow the Binary Search approach to calculate the square root of an integer x without using any in-built sqrt function.

# Since the square root of a number x lies between 0 and x/2 for all x >= 0, we can use binary search within this range (0 to x/2) to find the square root. The integer part (i.e., the floor) of the square root will be the final result.

import math

class Solution:
    def mySqrt(self, num:int) -> int:
        if num < 2:
            return num
        
        left, right = 2, num//2
        pivot = 0
        val = 0
        
        while left <= right:
            pivot = left + (right - left)//2
            val = pivot * pivot
            if val > num:
                right = pivot - 1
            elif val < num:
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