class Solution:
    def calculateSum(self, N):
        if N <= 0:
            return 0
        return N + self.calculateSum(N-1)

sol = Solution()
examples = [5, 10, 1]
for N in examples:
    sum = sol.calculateSum(N)
    print("Sum of first", N, "natural numbers:", sum)