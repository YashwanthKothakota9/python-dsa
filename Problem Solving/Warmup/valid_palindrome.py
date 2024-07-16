# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# This problem aims to check if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that read the same forward and backward, ignoring spaces, punctuation, and capitalization. Our algorithm can leverage the two-pointer technique where one pointer starts at the beginning of the string, and the other one starts at the end. The two pointers move towards each other, checking if the characters they point to are the same.

# Tc: O(n) Sc: O(1)

class Solution:
    def isPalindrome(self, s:str) -> bool:
        i, j = 0 , len(s)-1
        
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True

if __name__ == "__main__":
  sol = Solution()
  # Test case 1: "A man, a plan, a canal, Panama!"
  # Expected output: True
  print(sol.isPalindrome("A man, a plan, a canal, Panama!"))

  # Test case 2: "race a car"
  # Expected output: False
  print(sol.isPalindrome("race a car"))

  # Test case 3: "Was it a car or a cat I saw?"
  # Expected output: True
  print(sol.isPalindrome("Was it a car or a cat I saw?"))

  # Test case 4: "Madam, in Eden, I'm Adam."
  # Expected output: True
  print(sol.isPalindrome("Madam, in Eden, I'm Adam."))

  # Test case 5: "empty string"
  # Expected output: True
  print(sol.isPalindrome(""))
