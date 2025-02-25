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

class Solution:
    def isPalindromePossible(self, s:str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1) # type: ignore
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s:str, left:int, right:int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindromePossible("racecar"))  # true
    print(solution.isPalindromePossible("abccdba"))  # true
    print(solution.isPalindromePossible("abcdef"))   # false