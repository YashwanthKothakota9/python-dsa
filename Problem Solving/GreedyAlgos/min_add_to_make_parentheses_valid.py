# Given a string str containing '(' and ')' characters, find the minimum number of parentheses that need to be added to a string of parentheses to make it valid.

# A valid string of parentheses is one where each opening parenthesis '(' has a corresponding closing parenthesis ')' and vice versa. The goal is to determine the least amount of additions needed to achieve this balance.


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

# Initialization: Start with a counter set to zero, representing the number of parentheses needed to balance the string.

# Iterating through the String: For each character in the string, determine if it's an opening or closing parenthesis.

# Handling Opening Parenthesis: Increment the balance counter for each opening parenthesis, indicating a pending closing parenthesis is needed.

# Handling Closing Parenthesis: For each closing parenthesis, if there is an unmatched opening parenthesis (balance counter > 0), decrement the balance. If not, increment the counter, indicating an additional opening parenthesis is needed.

# Completion: The final value of the counter represents the total number of additional parentheses required to balance the string.

class Solution:
    def minAddToMakeValid(self, s:str) -> int:
        balance, counter = 0, 0
        for char in s:
            # Increment balance for '(', decrement for ')'
            balance += 1 if char == '(' else -1
            # If balance is negative, we have more ')' than '('
            if balance == -1:
                counter += 1 # Increment counter for each unmatched ')'
                balance += 1 # Reset balance as we've accounted for the unmatched ')'
        return counter + balance # Sum is the total adjustments needed

if __name__ == "__main__":
    solution = Solution()
    # Testing the algorithm with the three examples
    print(solution.minAddToMakeValid("(()"))        # Example 1
    print(solution.minAddToMakeValid("))(("))       # Example 2
    print(solution.minAddToMakeValid("(()())("))    # Example 3


# Time Complexity: The time complexity of this algorithm is O(n), where n is the length of the string. This is because we iterate through the string once.
# Space Complexity: The space complexity is O(1), as we only use a fixed amount of additional space (counter and balance variables) regardless of the input size.