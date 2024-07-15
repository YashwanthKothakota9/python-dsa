# Design a data structure that supports the addition of new words and the ability to check if a string matches any previously added word.

# Implement the Solution class:

# Solution() Initializes the object.
# void addWord(word) Inserts word into the data structure, making it available for future searches.
# bool search(word) Checks if there is any word in the data structure that matches word. The method returns true if such a match exists, otherwise returns false.
# Note: In the search query word, the character '.' can represent any single letter, effectively serving as a wildcard character.

# The crux of the problem lies in efficiently inserting words and then searching for them, even if the query includes wildcards. To solve this, we utilize the trie (prefix tree) data structure. A trie is a tree-like structure that's useful for storing a dynamic set of strings, especially when the dataset involves large numbers of queries on prefixes of strings. Each node of the trie can represent a character of a word, and the path from the root node to any node represents the word stored up to that point. The key operation for the wildcard is a recursive search, which allows us to explore multiple paths in the trie when we encounter the wildcard character.

# 1. Trie Data Structure: Every node of the trie contains multiple child nodes (one for each character of the alphabet). We start with a root node that represents an empty string. Each level of the trie represents the next character of a word.

# 2. Adding a Word: To insert a word into our trie, we begin at the root and traverse down the trie based on the characters in the word. If a particular character doesn't have a corresponding child node in the current node, we create a new child node for that character. Once we've processed every character of the word, we mark the final node as the end of a valid word.

# 3. Searching: Searching for a word is similar to inserting, but with an additional consideration for the wildcard character ('.'). If we encounter a '.', we must consider all child nodes of the current node and recursively continue our search from each of them. If any of the paths result in a match, we return true. If we reach the end of a word without encountering any mismatches or premature ends, we've found a valid word in our trie.

# This trie-based approach ensures efficient operations for both inserting and searching for words. In cases without wildcards, the search operation can be performed in linear time relative to the word's length. However, with wildcards, the time complexity might increase, but the trie structure still ensures that we do this efficiently.

# Time Complexity:
# Insertion (addWord): O(n), where n is the length of the word. This is because each insertion operation runs in linear time with respect to the length of the word.
# Search: O(n * m) in the worst case, where n is the length of the word and m is the total number of nodes in the Trie. This happens when the search word contains dots ('.'). However, for words without dots, the search is O(n).
# Space Complexity: O(m * n), where m is the total number of Trie nodes and n is the average number of characters in the words. Each Trie node has up to 26 children (for each letter of the alphabet). In the worst case, when no nodes are shared, the space complexity is O(m * n).


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def addWord(self, word:str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
    
    def search(self, word:str) -> bool:
        return self.searchInNode(word, self.root)
    
    def searchInNode(self, word:str, node: TrieNode) -> bool:
        for i,ch in enumerate(word):
            if ch == '.':
                return any(self.searchInNode(word[i+1:],node.children[child]) for child in node.children if child)
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd
    
obj = Solution()
obj.addWord("apple")
obj.addWord("banana")
print(obj.search("apple"))  # True
print(obj.search("....."))  # True