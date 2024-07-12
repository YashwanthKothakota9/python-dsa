# Given a string str containing '(' and ')' characters, find the minimum number of parentheses that need to be added to a string of parentheses to make it valid.

# A valid string of parentheses is one where each opening parenthesis '(' has a corresponding closing parenthesis ')' and vice versa. The goal is to determine the least amount of additions needed to achieve this balance.

# Examples
# Example 1:

# Input: "(()"
# Expected Output: 1
# Justification: The string has two opening parentheses and one closing parenthesis. Adding one closing parenthesis at the end will balance it.
# Example 2:

# Input: "))(("
# Expected Output: 4
# Justification: There are two closing parentheses at the beginning and two opening at the end. We need two opening parentheses before the first closing and two closing parentheses after the last opening to balance the string.
# Example 3:

# Input: "(()())("
# Expected Output: 1
# Justification: The string has three opening parentheses and three closing parentheses, with an additional opening parenthesis at the end. Adding one closing parenthesis at the end will balance it.


# To solve this problem, we track the balance of parentheses as we iterate through the string. We initialize two counters: one for the balance of parentheses and another for the count of additions needed.

# For each character in the string, if it's an opening parenthesis '(', we increase the balance. If it's a closing parenthesis ')', we decrease the balance. If the balance is negative at any point (which means there are more closing parentheses than opening ones), we increment the additions counter and reset the balance to zero.

# The total number of additions required is the sum of the additions counter and the absolute value of the final balance, ensuring that all unmatched opening parentheses are also accounted for. This approach efficiently computes the minimum number of parentheses to be added for the string to become valid.

class Solution:
    def minAddToMakeValid(self, s:str)->int:
        balance, counter = 0, 0
        for char in s:
            balance += 1 if char == '(' else -1
            if balance == -1:
                counter += 1
                balance += 1
        return counter + balance

if __name__ == "__main__":
    solution = Solution()
    # Testing the algorithm with the three examples
    print(solution.minAddToMakeValid("(()"))        # Example 1
    print(solution.minAddToMakeValid("))(("))       # Example 2
    print(solution.minAddToMakeValid("(()())("))    # Example 3


