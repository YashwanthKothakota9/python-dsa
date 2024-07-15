# Write a Recursive Approach to Check if a Given Digit String Represents a Good Number.

# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime ((2, 3, 5, or 7).


class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def isGoodNumber(self, digits, index):
        if index >= len(digits):
            return True  # Base case: reached the end of the string

        digit = digits[index]

        # Check if the digit at the current index satisfies the conditions
        if (index % 2 == 0 and int(digit) % 2 != 0) or (index % 2 != 0 and not self.is_prime(int(digit))):
            return False

        # Recursively check the next digit
        return self.isGoodNumber(digits, index + 1)


sol = Solution()
digit_strings = ["02468", "23478", "123456"]

for digits in digit_strings:
    is_good = sol.isGoodNumber(digits, 0)
    print(f"Digit string: {digits} is {'good' if is_good else 'not good'}")