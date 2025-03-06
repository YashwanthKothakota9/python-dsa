# Given a string s and an integer k, return the highest number of vowels in any substring of s that is exactly k characters long. Vowels in English are 'a', 'e', 'i', 'o', and 'u'.

# Examples
# Example 1:

# Input: s = "azerdii", k = 4
# Expected Output: 2
# Justification: The substring "rdii" has two vowels ('i', 'i').
# Example 2:

# Input: s = "abcde", k = 2
# Expected Output: 1
# Justification: The substring "ab" contains one vowel ('a').
# Example 3:

# Input: s = "zaeixoyuxyz", k = 7

# Solution
# To solve this problem, we will use a sliding window approach. This method allows us to efficiently keep track of the number of vowels in any substring of length k as we move through the string. We start by counting the vowels in the first k characters. Then, we slide the window one character to the right at a time, adjusting the vowel count by subtracting the character that is left behind and adding the new character that enters the window.

# This approach is effective because it avoids recalculating the number of vowels from scratch for every substring, which would be inefficient. Instead, it updates the count in constant time, making the overall time complexity linear in relation to the length of the string.

# Algorithm Walkthrough
# Let's consider the input: s = "zaeixoyuxyz", k = 7

# Initialization:

# maxVowels = 0
# currentVowels = 0
# Define isVowel(char ch) to check if a character is 'a', 'e', 'i', 'o', or 'u'.
# First Window Setup (characters: 'z', 'a', 'e', 'i', 'x', 'o', 'y'):

# i = 0, s[0] = 'z' → Not a vowel, currentVowels = 0
# i = 1, s[1] = 'a' → Vowel, currentVowels = 1
# i = 2, s[2] = 'e' → Vowel, currentVowels = 2
# i = 3, s[3] = 'i' → Vowel, currentVowels = 3
# i = 4, s[4] = 'x' → Not a vowel, currentVowels = 3
# i = 5, s[5] = 'o' → Vowel, currentVowels = 4
# i = 6, s[6] = 'y' → Not a vowel, currentVowels = 4
# Store Initial Count:

# maxVowels = 4
# Sliding Window:

# i = 7, s[7] = 'u' → Vowel, currentVowels = 5

# s[7-7] = s[0] = 'z' → Not a vowel, currentVowels = 5
# maxVowels = max(4, 5) = 5
# i = 8, s[8] = 'x' → Not a vowel, currentVowels = 5

# s[8-7] = s[1] = 'a' → Vowel, currentVowels = 4
# maxVowels = max(5, 4) = 5
# i = 9, s[9] = 'y' → Not a vowel, currentVowels = 4

# s[9-7] = s[2] = 'e' → Vowel, currentVowels = 3
# maxVowels = max(5, 3) = 5
# i = 10, s[10] = 'z' → Not a vowel, currentVowels = 3

# s[10-7] = s[3] = 'i' → Vowel, currentVowels = 2
# maxVowels = max(5, 2) = 5
# Return Result:

# Return maxVowels = 5

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the string. This is because we scan the string once to initialize the first window and then slide the window across the string.
# Space Complexity: O(1). We use a constant amount of extra space regardless of the size of the input.

class Solution:
    def maxVowels(self, s: str, k: int):
        def is_vowel(ch):
            return ch in 'aeiou'

        max_vowels = 0
        curr_vowels = 0

        for i in range(k):
            if is_vowel(s[i]):
                curr_vowels += 1

        max_vowels = curr_vowels

        for i in range(k, len(s)):
            if is_vowel(s[i]):
                curr_vowels += 1
            if is_vowel(s[i-k]):
                curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels("azerdii", 4))  # Output: 2
    print(solution.maxVowels("abcde", 2))   # Output: 1
    print(solution.maxVowels("zaeixoyuxyz", 7))  # Output: 5
