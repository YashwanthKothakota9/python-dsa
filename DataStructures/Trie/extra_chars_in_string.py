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

class TrieNode:
    def __init__(self):
        self.children = {}  # Represents each character of the alphabet.
        self.isEnd = False  # To determine if the current TrieNode marks the end of a word.

class Solution:
    def minExtraChar(self, s, dictionary):
        root = self.buildTree(dictionary)
        n = len(s)
        # DP array to store minimum extra characters.
        dp = [0]*(n+1)
        
        for start in range(n-1,-1,-1):
            # Default case: considering current character as extra.
            dp[start] = dp[start+1]+1
            node = root
            for end in range(start, n):
                if 'a' <= s[end] <= 'z':
                    if s[end] not in node.children:
                        break
                    node = node.children[s[end]]
                    if node.isEnd:
                        dp[start] = min(dp[start], dp[end+1])
                else:
                    raise ValueError(f"Invalid char {s[end]} in string")
        # Minimum extra characters for the entire string.
        print(dp)
        return dp[0]
    
    def buildTree(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if 'a' <= char <= 'z':
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                else:
                    raise ValueError(f"Invalid char {char} in dictionary {word}")
            node.isEnd = True
        return root


def main():
    solution = Solution()
    print(solution.minExtraChar("amazingracecar", ["race", "car"]))  # Output: 7
    print(solution.minExtraChar("bookkeeperreading", ["keep", "read"]))  # Output: 9
    print(solution.minExtraChar("thedogbarksatnight", ["dog", "bark", "night"]))  # Output: 6

if __name__ == "__main__":
    main()