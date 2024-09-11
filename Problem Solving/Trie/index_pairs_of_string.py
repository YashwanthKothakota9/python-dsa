# Given a string text and a list of strings words, identify all [i, j] index pairs such that the substring text[i...j] is in words.

# These index pairs should be returned in ascending order, first by the start index, then by the end index. Find every occurrence of each word within the text, ensuring that overlapping occurrences are also identified.

# Examples
# Input: text = "bluebirdskyscraper", words = ["blue", "bird", "sky"]
# Expected Output: [[0, 3], [4, 7], [8, 10]]
# Justification: The word "blue" is found from index 0 to 3, "bird" from 4 to 7, and "sky" from 8 to 10 in the string.
# Input: text = "programmingisfun", words = ["pro", "is", "fun", "gram"]
# Expected Output: [[0, 2], [3, 6], [11, 12], [13, 15]]
# Justification: "pro" is found from 0 to 2, "gram" from 3 to 6, "is" from 11 to 12, and "fun" from 13 to 15.
# Input: text = "interstellar", words = ["stellar", "star", "inter"]
# Expected Output: [[0, 4], [5, 11]]
# Justification: "inter" is found from 0 to 4, and "stellar" from 5 to 11. "star" is not found.

# To solve this problem, we will use a trie data structure, which is particularly efficient for managing a set of strings and performing quick searches for patterns within a text. A trie, also known as a prefix tree, allows us to efficiently store and retrieve strings with a common prefix, making it ideal for our purpose of identifying substrings within a given text.

# The approach involves two main phases: building the trie with the given list of words and then using it to find the index pairs in the text. The trie's structure enables us to search for each word in the text in an optimized manner, significantly reducing the number of comparisons needed compared to brute force methods.

class TrieNode:
    def __init__(self):
        self.children = {}  # Using a dictionary to hold child nodes for each letter
        self.isEnd = False  # Flag to mark the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                # Create a new node if not present
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEnd = True  # Mark the end of a word


class Solution:
    def indexPairs(self, text, words):
        trie = Trie()
        # Populate the trie with the list of words
        for word in words:
            trie.insert(word)

        result = []
        for i in range(len(text)):
            p = trie.root
            for j in range(i, len(text)):
                currChar = text[j]
                if currChar not in p.children:
                    break  # Break if the character is not in the trie
                p = p.children[currChar]
                if p.isEnd:
                    # Add index pair if word found as a list
                    result.append([i, j])

        return result  # Return a list of lists containing index pairs


solution = Solution()
text1 = "bluebirdskyscraper"
words1 = ["blue", "bird", "sky"]
print(solution.indexPairs(text1, words1))

text2 = "programmingisfun"
words2 = ["pro", "is", "fun", "gram"]
print(solution.indexPairs(text2, words2))

text3 = "interstellar"
words3 = ["stellar", "star", "inter"]
print(solution.indexPairs(text3, words3))


# Time Complexity:
# Building the Trie: O(N*L), where N is the number of words and L is the average length of these words.
# Finding Index Pairs: O(T^2), where T is the length of the text string.
# Overall: O(N*L+T^2)
# Space Complexity:
# Trie Storage: O(N*L), for storing N words each of average length L.
