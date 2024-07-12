# Base Case:
# If the given number is 0 or 1, return true because 0 and 1 are perfect squares.
# Recursive Case:
# The algorithm performs a binary search to find the square root of the number and check if it is a perfect square.
# Calculate the mid value between a lower bound and an upper bound.
# Check if the square of the mid value is equal to the given number.
# If it is equal, return true because the number is a perfect square.
# If it is less than the given number, make a recursive call with an updated lower bound of mid + 1.
# If it is greater than the given number, make a recursive call with an updated upper bound of mid - 1.


class Solution:
    def isPerfSquare(self, num):
        
        def isPerfSquareHelper(num, low, high):
            if low > high:
                return False
            mid = (low+high)//2
            if mid*mid == num:
                return True
            elif mid * mid > num:
                return isPerfSquareHelper(num, low, mid-1)
            else:
                return isPerfSquareHelper(num, mid+1, high)
        
        return isPerfSquareHelper(num, 0, num)

sol = Solution()
examples = [16, 14, 9]
for num in examples:
    isPerfect = sol.isPerfSquare(num)
    print(f"{num} is a perfect square: {isPerfect}")