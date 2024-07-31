# Given a string, identify the position of the first character that appears only once in the string. If no such character exists, return -1.

# Examples

# Example 1:

# Input: "apple"
# Expected Output: 0
# Justification: The first character 'a' appears only once in the string and is the first character.
# Example 2:

# Input: "abcab"
# Expected Output: 2
# Justification: The first character that appears only once is 'c' and its position is 2.

# To solve this problem, we'll use a hashmap to keep a record of each character in the string and the number of times it appears. First, iterate through the string and populate the hashmap with each character as the key and its frequency as the value. Then, go through the string again, this time checking each character against the hashmap. The first character that has a frequency of one (indicating it doesn't repeat) is your target. This character is the first non-repeating character in the string. If no such character exists, the solution should indicate that as well. This two-pass approach ensures efficiency, as each character is checked against a pre-compiled frequency map.


class Solution:
    def firstUniqueChar(self, s:str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqueChar("apple"))  # Expected: 0
    print(sol.firstUniqueChar("abcab"))  # Expected: 2
    print(sol.firstUniqueChar("abab"))   # Expected: -1

# Tc: O(N) Sc: O(1)