# The algorithm to check if a number is prime or not using recursion can be defined as follows:

# If the number is less than 2, return false (base case).
# If the number is equal to 2, return true (base case).
# If the number is divisible by any number from 2 to the square root of the number, return false.
# Otherwise, return true.

class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        return self.checkDivisors(num, 2)
    
    def checkDivisors(self,num,divisor):
        if divisor > num ** 0.5:
            return True
        if num % divisor == 0:
            return False
        return self.checkDivisors(num, divisor+1)
    
sol = Solution()
examples = [7, 12, 23]

for example in examples:
    is_prime_result = sol.isPrime(example)
    print(f"{example} is prime: {is_prime_result}")