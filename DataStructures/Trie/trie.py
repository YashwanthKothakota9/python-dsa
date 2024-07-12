class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word):
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]: # type: ignore
                node.children[index] = TrieNode() # type: ignore
            node = node.children[index] # type: ignore
    
    def search(self, word):
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]: # type: ignore
                return False
            node = node.children[index] # type: ignore
        return node.isEndOfWord # type: ignore
    
    def _delete(self, current, word, index):
        if index == len(word):
            if current.isEndOfWord:
                current.isEndOfword = False
                return not any(current.children)
            return False
        ch = word[index]
        node = current.children[self.charToIndex(ch)]
        if not node:
            return False
        shouldDeleteChild = self._delete(node, word, index+1)
        if shouldDeleteChild:
            current.children[self.charToIndex(ch)] = None
            return not any(current.children)
        return False
    
    def deleteWord(self, word):
        self._delete(self.root, word, 0)