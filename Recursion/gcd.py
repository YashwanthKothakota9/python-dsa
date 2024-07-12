class Solution:
    def gcd(self, A, B):
        if B==0:
            return A
        return self.gcd(B, A%B)

examples = [[12, 18], [25, 15], [40, 60]]
sol = Solution()

for example in examples:
    A, B = example
    gcd = sol.gcd(A, B)
    print("GCD of", A, "and", B, "is:", gcd)