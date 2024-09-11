# Given a string s and an array of words words. Break string s into multiple non-overlapping substrings such that each substring should be part of the words. There are some characters left which are not part of any substring.

# Return the minimum number of remaining characters in s, which are not part of any substring after string break-up.

# Examples
# Example 1:

# Input: s = "amazingracecar", dictionary = ["race", "car"]
# Expected Output: 7
# Justification: The string s can be rearranged to form "racecar", leaving 'a', 'm', 'a', 'z', 'i', 'n', 'g' as extra.
# Example 2:

# Input: s = "bookkeeperreading", dictionary = ["keep", "read"]
# Expected Output: 9
# Justification: The words "keep" and "read" can be formed from s, but 'b', 'o', 'o', 'k', 'e', 'r', 'i', 'n', 'g' are extra.
# Example 3:

# Input: s = "thedogbarksatnight", dictionary = ["dog", "bark", "night"]
# Expected Output: 6
# Justification: The words "dog", "bark", and "night" can be formed, leaving 't', 'h', 'e', 's', 'a', 't' as extra characters.

# The solution approach utilizes a dynamic programming strategy combined with a trie data structure. The dynamic programming aspect allows for efficiently keeping track of the minimum extra characters required at each position in the string s. This is achieved by building a bottom-up solution, where we start from the end of the string and work our way towards the beginning, calculating the minimum extra characters required for each substring.

# The trie data structure is used to efficiently find and match the words from the dictionary within the string s. The combination of these two methods ensures that the solution is both time-efficient and space-efficient, as it avoids redundant computations and efficiently manages the storage of the dictionary words.

# Step-by-Step Algorithm
# Initialize Trie:

# Construct a trie using the words from the dictionary. Each node in the trie represents a character, and a complete path from the root to a leaf node represents a word.
# Dynamic Programming Array:

# Initialize a dynamic programming (DP) array, dp, of length n + 1, where n is the length of the string s. This array will store the minimum number of extra characters required for the substring starting from each index.
# DP Calculation:

# Iterate backwards through the string s:
# Set dp[start] to dp[start + 1] + 1 initially. This represents the case where the current character is considered an extra character.
# For each start position, iterate through the string to check if a word in the trie can be formed starting from this position.
# If the current substring matches a word in the trie (node.isEnd is true), update dp[start] to be the minimum of its current value and dp[end + 1], where end is the end of the matched word. This step ensures that we consider removing the matched word and count the rest as extra characters.
# Return Result:

# The value of dp[0] gives the minimum number of extra characters in the entire string s.

# This approach systematically checks each substring of s against the trie, and the dynamic programming array efficiently keeps track of the minimum extra characters required. The use of a trie ensures that each substring check is done in an optimized manner, avoiding unnecessary recomputations.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def minExtraChar(self, s, dict):
        root = self.buildTrie(dict)
        n = len(s)
        dp = [0]*(n+1)

        for start in range(n-1, -1, -1):
            # Default case: considering current character as extra.
            dp[start] = dp[start+1]+1

            node = root
            for end in range(start, n):
                if 'a' <= s[end] <= 'z':  # Ensure the character is a lowercase letter
                    if s[end] not in node.children:
                        break  # No further word can be formed.
                    node = node.children[s[end]]
                    if node.isEnd:
                        dp[start] = min(dp[start], dp[end + 1])
                else:
                    raise ValueError(f"Invalid character {s[end]} in string")

        return dp[0]  # Minimum extra characters for the entire string.

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if 'a' <= char <= 'z':  # Ensure the character is a lowercase letter
                    if char not in node.children:
                        # Creating new node if not exists.
                        node.children[char] = TrieNode()
                    node = node.children[char]
                else:
                    raise ValueError(
                        f"Invalid character {char} in dictionary word {word}")
            node.isEnd = True  # Mark the end of a word.
        return root


def main():
    solution = Solution()
    print(solution.minExtraChar(
        "amazingracecar", ["race", "car"]))  # Output: 7
    print(solution.minExtraChar(
        "bookkeeperreading", ["keep", "read"]))  # Output: 9
    print(solution.minExtraChar("thedogbarksatnight",
          ["dog", "bark", "night"]))  # Output: 6


if __name__ == "__main__":
    main()


# Time Complexity
# Trie Construction: (O(W x L)), where (W) is the number of words in the dictionary and (L) is the average length of these words.
# Dynamic Programming Calculation: (O(n^2)), where (n) is the length of the input string s.
# Total Time Complexity: (O(W x L + n^2)).
# Space Complexity
# Trie Storage: (O(W x L)), for storing the words in the trie.
# Dynamic Programming Array: (O(n)), for the array used in dynamic programming.
# Total Space Complexity: (O(W x L + n)).
