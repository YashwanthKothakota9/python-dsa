# Write a Recursive Approach to Calculate Power of Integer to N Pow(x,n).

# Given an integer x and an integer n, write a recursive function to calculate the power of x to the nth power.

# If n is equal to 0, return 1 since any number raised to the power of 0 equals 1.
# If n is less than 0, return 1 divided by the result of calculating x raised to the power of -n.
# If n is greater than 0, recursively calculate x raised to the power of n/2. Store the result in a variable temp.
# If n is even, return the square of temp (i.e., temp * temp).
# If n is odd, return x multiplied by the square of temp (i.e., x * temp * temp).


# The time complexity of this algorithm is O(logN) because we divide the problem size in half with each recursive call. The space complexity is O(logN) as well because the maximum depth of the recursion is log n.

class Solution:
    def calcPower(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.calcPower(x, -n)
        temp = float(self.calcPower(x, n//2))
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp

sol = Solution()

x1, n1 = 2, 5
x2, n2 = 3, 4
x3, n3 = 5, 0

# Calculate power and print results
print(f"Power of {x1} to the power of {n1} = {sol.calcPower(x1, n1)}")
print(f"Power of {x2} to the power of {n2} = {sol.calcPower(x2, n2)}")
print(f"Power of {x3} to the power of {n3} = {sol.calcPower(x3, n3)}")