# Given the Roman numeral string s, convert it into its equivalent integer and return it.

# Roman numerals use combinations of seven symbols: I, V, X, L, C, D, and M, representing values 1, 5, 10, 50, 100, 500, and 1000 respectively.

# For example, I is equivalent to 1, II is equivalent to 2, and XI is equivalent to 11 (X + I). In some cases, a smaller numeral before a larger numeral indicates subtraction (e.g., IV = 4).

# Example 1:

# Input: s = "XLII"
# Output: 42
# Justification: L (50) - X (10) + I (1) + I (1) = 42
# Example 2:

# Input: s = "CXCIV"
# Output: 194
# Justification: C (100) - X (10) + C (100) - I (1) + V (5) = 194
# Example 3:

# Input: s = "MMMCDXLIV"
# Output: 3444
# Justification: M (1000) + M (1000) + M (1000) - C (100) + D (500) - X (10) + L (50) - I (1) + V (5) = 3444


# To solve this problem, we will iterate through the Roman numeral string from left to right. We will use a dictionary to map Roman symbols to their integer values. If the current symbol represents a value smaller than the next symbol, it means we need to subtract this value. Otherwise, we add the current value to the total sum. This approach ensures we correctly handle both addition and subtraction cases in Roman numerals.

# This approach works because it simplifies the problem into a series of comparisons and additions or subtractions. By checking each symbol against the next, we ensure that the unique rules of Roman numeral subtraction are adhered to without needing complex logic or nested conditions.

# Step-by-Step Algorithm
# Create a dictionary to map Roman numerals to their integer values.
# Initialize a variable total to store the final integer value.
# Iterate through the string:
# If the current symbol's value is less than the next symbol's value, subtract the current symbol's value from total.
# Otherwise, add the current symbol's value to total.
# Return the total as the converted integer value.

# Input: s = "MMMCDXLIV"

# Initialize result to 0.

# Create a dictionary of Roman numerals to integers:

# {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# Iterate through the string "MMMCDXLIV":

# Iteration 1:

# Current character: 'M'
# Value: 1000
# Next character: 'M'
# Since 1000 >= 1000, add 1000 to result.
# result = 0 + 1000 = 1000
# Iteration 2:

# Current character: 'M'
# Value: 1000
# Next character: 'M'
# Since 1000 >= 1000, add 1000 to result.
# result = 1000 + 1000 = 2000
# Iteration 3:

# Current character: 'M'
# Value: 1000
# Next character: 'C'
# Since 1000 >= 100, add 1000 to result.
# result = 2000 + 1000 = 3000
# Iteration 4:

# Current character: 'C'
# Value: 100
# Next character: 'D'
# Since 100 < 500, subtract 100 from result.
# result = 3000 - 100 = 2900
# Iteration 5:

# Current character: 'D'
# Value: 500
# Next character: 'X'
# Since 500 >= 10, add 500 to result.
# result = 2900 + 500 = 3400
# Iteration 6:

# Current character: 'X'
# Value: 10
# Next character: 'L'
# Since 10 < 50, subtract 10 from result.
# result = 3400 - 10 = 3390
# Iteration 7:

# Current character: 'L'
# Value: 50
# Next character: 'I'
# Since 50 >= 1, add 50 to result.
# result = 3390 + 50 = 3440
# Iteration 8:

# Current character: 'I'
# Value: 1
# Next character: 'V'
# Since 1 < 5, subtract 1 from result.
# result = 3440 - 1 = 3439
# Iteration 9:

# Current character: 'V'
# Value: 5
# No next character
# Add 5 to result.
# result = 3439 + 5 = 3444
# Final result is 3444.

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the input string. We iterate through the string once, performing constant-time operations for each character.
# Space Complexity: O(1), since the size of the dictionary is fixed and does not grow with the input size.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        n = len(s)
        # Iterate through the string
        for i in range(n):
            # Get the value of the current Roman numeral
            value = roman_map[s[i]]
            # Check if the current numeral is smaller than the next one
            if i < n-1 and value < roman_map[s[i+1]]:
                result -= value
            else:
                result += value
        return result


solution = Solution()
print(solution.romanToInt("XLII"))  # 42
print(solution.romanToInt("CXCIV"))  # 194
print(solution.romanToInt("MMMCDXLIV"))  # 3444
