# Design and implement a Trie(also known as a Prefix Tree). A trie is a tree-like data structure that stores a dynamic set of strings, and is particularly useful for searching for words with a given prefix.

# Implement the Solution class:

# Solution() Initializes the object.
# void insert(word) Inserts word into the trie, making it available for future searches.
# bool search(word) Checks if the word exists in the trie.
# bool startsWith(word) Checks if any word in the trie starts with the given prefix.
# Examples
# Example 1:

# Input:
# Trie operations: ["Trie", "insert", "search", "startsWith"]
# Arguments: [[], ["apple"], ["apple"], ["app"]]
# Expected Output: [-1, -1, 1, 1]
# Justification: After inserting "apple", "apple" exists in the Trie. There is also a word that starts with "app", which is "apple".
# Example 2:

# Input:
# Trie operations: ["Trie", "insert", "search", "startsWith", "search"]
# Arguments: [[], ["banana"], ["apple"], ["ban"], ["banana"]]
# Expected Output: [-1, -1, 0, 1, 1]
# Justification: After inserting "banana", "apple" does not exist in the Trie but a word that starts with "ban", which is "banana", does exist.
# Example 3:

# Input:
# Trie operations: ["Trie", "insert", "search", "startsWith", "startsWith"]
# Arguments: [[], ["grape"], ["grape"], ["grap"], ["gr"]]
# Expected Output: [-1, -1, 1, 1, 1]
# Justification: After inserting "grape", "grape" exists in the Trie. There are words that start with "grap" and "gr", which is "grape".

# The trie is represented as a tree, where each node contains an array of pointers (or references) to its children and a boolean flag indicating if the current node marks the end of a word. When inserting or searching for a word, we start at the root node and navigate through the tree character by character until we either finish the operation or determine the word doesn't exist in the trie.

# Now, let's break down the operations:

# Insert:

# We begin at the root node.
# For every character in the word, check if there's a child node for it.
# If the child node doesn't exist, we create it.
# Navigate to the child node and repeat the process for the next character.
# Once the end of the word is reached, mark the current node as an endpoint of a word.
# Search:

# Starting at the root, traverse the trie character by character.
# For every character in the word, check if there's a child node for it.
# If at any point there isn't a child node for the character, the word doesn't exist in the trie.
# If we can traverse the entire word and the last node is marked as an endpoint, the word exists in the trie.
# StartsWith:

# The operation is similar to the search, but we don't need the last node to be an endpoint.
# If we can traverse the prefix without any missing nodes, there exists a word in the trie that starts with the given prefix.

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes.
        self.isEnd = False  # Flag to represent end of a word.


class Solution:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Solution()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))    # False
    print(trie.startsWith("app"))  # True

# Complexity Analysis
# Time Complexity:
# Insert: O(m), where m is the key length.
# Search and StartsWith: O(m) in the worst case scenario.
# Space Complexity: O(n*m), where n is the number of inserted keys and m is the average key length.
