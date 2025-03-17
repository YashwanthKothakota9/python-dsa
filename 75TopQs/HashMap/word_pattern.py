# Given a pattern and a string s, return true if the string s follows the same pattern.

# Here, the following the pattern means each character in the pattern should map to a single word in s, and each word in s should map to a single character in the pattern.

# Examples
# Example 1:

# Input: pattern = "eegg", s = "dog dog cat cat"
# Output: true
# Explanation: The pattern "eegg" corresponds to the words "dog dog cat cat". Both 'e's map to "dog" and both 'g's map to "cat".
# Example 2:

# Input: pattern = "abca", s = "one two three four"
# Output: false
# Explanation: Here, a maps to the "one" and "four" both. So, the string doesn't follow the same pattern.
# Example 3:

# Input: pattern = "abacac", s = "dog cat dog mouse dog mouse"
# Output: true
# Explanation: The pattern "abacac" corresponds to the words "dog cat dog mouse dog mouse". 'a' maps to "dog", 'b' maps to "cat", and 'c' maps to "mouse".
# Solution
# To solve this problem, we need to establish a one-to-one correspondence between each character in the pattern and each word in the string s. This can be effectively managed using two hash maps: one to map characters from the pattern to words in s, and another to map words in s to characters in the pattern. This dual mapping ensures that the relationship is consistent in both directions. If at any point we find that a character or word does not map as expected, we can conclude that string does not follow the pattern.

# This approach is efficient because it allows us to quickly check and establish the required mappings. The use of hash maps ensures that our checks and insertions are done in constant time on average, making the overall approach fast and reliable.

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the pattern or the number of words in s. We iterate through the pattern and the words once, performing constant-time operations (hash map lookups and insertions) at each step.
# Space Complexity: O(n), where n is the number of unique characters in the pattern or unique words in s. In the worst case, we store every character and word in the hash maps.

class Solution:
    def pattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
                else:
                    char_to_word[char] = word
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
                else:
                    word_to_char[word] = char

        return True


if __name__ == "__main__":
    solution = Solution()
    # Example 1
    print(solution.pattern("eegg", "dog dog cat cat"))  # true
    # Example 2
    print(solution.pattern("abca", "one two three four"))  # false
    # Example 3
    print(solution.pattern("abacac", "dog cat dog mouse dog mouse"))  # true
