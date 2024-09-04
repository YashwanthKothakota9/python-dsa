# This task involves checking if a given string can be turned into a palindrome by removing at most
# one character. To achieve this, you can follow these steps:
# Given string s, determine whether it's possible to make a given string palindrome by removing at most one character.

# A palindrome is a word or phrase that reads the same backward as forward.

# Examples
# Example 1:

# Input: "racecar"
# Expected Output: true
# Justification: The string is already a palindrome, so no removals are needed.
# Example 2:

# Input: "abeccdeba"
# Expected Output: true
# Justification: Removing the character 'd' forms the palindrome "abccba".
# Example 3:

# Input: "abcdef"
# Expected Output: false
# Justification: No single character removal will make this string a palindrome.


# To solve this problem, we use a two-pointer approach that initiates at both ends of the string. These pointers move towards the center, comparing characters at each step. Upon encountering a mismatch, the algorithm decides whether to skip the character at the left or the right pointer. A helper function is used to check if the resulting substring (after skipping a character) forms a palindrome. This process is performed twice, once for each pointer. If either scenario results in a palindrome, the original string can be considered a valid palindrome after removing at most one character. This efficient method determines the feasibility of forming a palindrome with minimal alterations to the string.

# Initialization: Begin by initializing the left pointer with 0 and the right pointer with n - 1, where n is a string length.

# Two-Pointer Traversal: Use two pointers, and move these pointers towards the center, comparing the characters at each step.

# Handling Mismatch: Upon encountering a mismatch, the algorithm checks two scenarios: removing the character at the left pointer or at the right pointer. For each scenario, it checks if the remaining substring forms a palindrome.

# Greedy Decision Making: If either resulting substring is a palindrome, return true. This decision is based on the greedy principle that choosing the first viable option (resulting in a palindrome) is sufficient.

# Concluding Result: If neither scenario results in a palindrome, the algorithm concludes that it's impossible to form a palindrome by removing just one character and returns false.

# This greedy approach is efficient as it minimizes the number of checks needed to determine if the string can be a valid palindrome with a single character removal.

class Solution:
    def isPalindromePossible(self, s:str)->bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left]!=s[right]:
                # Check if either substring (after removing one char) is a palindrome
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s:str, left:int, right:int) -> bool:
        while left < right:
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindromePossible("racecar"))  # true
    print(solution.isPalindromePossible("abccdba"))  # true
    print(solution.isPalindromePossible("abcdef"))   # false


# Time Complexity: O(n) for traversing the string.
# Space Complexity: O(1) as no extra space is used.