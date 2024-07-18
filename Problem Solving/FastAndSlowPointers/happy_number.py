# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to the number 1. All other (not-happy) numbers will never reach 1. Instead, they will be stuck in a cycle of numbers that does not include 1.

# Given a positive number n, return true if it is a happy number otherwise return false.

# Input: 23
# Output: true (23 is a happy number)
# Explanations: Here are the steps to find out that 23 is a happy number:

#  2^2 + 3^2 = 4 + 9 = 13
#  1^2 + 3^2 = 1 + 9 = 10
#  1^2 + 0^2 = 1 + 0 = 1

# Tc: O(logN) Sc: O(1)

class Solution:
    def find(self, num):
        slow, fast = num, num
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1
    
    def find_square_sum(self, num):
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10
        return _sum

def main():
  sol = Solution()
  print(sol.find(23))
  print(sol.find(12))


main()