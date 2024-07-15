class Solution:
    def __init__(self):
        self.memoization_table = {}
    
    def fibonacci(self, n):
        if n == 0 or n == 1:
            return n
        if n in self.memoization_table:
            return self.memoization_table[n]
        fib = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.memoization_table[n] = fib
        return fib

sol = Solution()
examples = [5, 8, 12]
for n in examples:
    print(f"Fibonacci Series up to {n}: ", end="")
    for i in range(n + 1):
        print(sol.fibonacci(i), end=" ")
    print()
