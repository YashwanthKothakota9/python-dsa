class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str)->None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd
    
    def startsWith(self, prefix:str)->bool:
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
    print(trie.startsWith("app"))# True        
    
# Time Complexity:
# Insert:O(m) , where m is the key length.
# Search and StartsWith: O(m) in the worst case scenario.
# Space Complexity:O(n*m) , where n  is the number of inserted keys and m is the average key length.
