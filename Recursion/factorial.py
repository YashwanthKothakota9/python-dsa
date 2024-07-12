class Solution:
    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        return num * self.factorial(num-1)

examples = [5, 7, 1]
sol = Solution()

for number in examples:
    factorial = sol.factorial(number)
    print("Factorial of", number, ":", factorial)