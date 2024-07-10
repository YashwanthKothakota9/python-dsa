# Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

# Input: 18
# Output: "10010"
# Explanation: The binary equivalent of 18 is 10010.


# Tc: O(logn) Sc: O(logn)
class Solution:
    def decimal_to_binary(self,num):
        stack = []
        while num > 0:
            stack.append(num%2)
            num = num // 2
        return ''.join(str(i) for i in reversed(stack))

def main():
    sol = Solution()
    print(sol.decimal_to_binary(2))    # Output: "10" (Binary representation of 2)
    print(sol.decimal_to_binary(7))    # Output: "111" (Binary representation of 7)
    print(sol.decimal_to_binary(18))   # Output: "10010" (Binary representation of 18)

if __name__ == '__main__':
    main()

