class Solution:
    def decimalToBinary(self, n):
        if n == 0:
            return ""
        return self.decimalToBinary(n//2) + str(n%2)

sol = Solution()
examples = [10, 27, 5]

for example in examples:
    binary = sol.decimalToBinary(example)
    print("Binary representation of", example, "is:", binary)