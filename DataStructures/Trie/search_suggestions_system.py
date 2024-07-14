# Given a list of distinct strings products and a string searchWord.

# Determine a set of product suggestions after each character of the search word is typed. Every time a character is typed, return a list containing up to three product names from the products list that have the same prefix as the typed string.

# If there are more than 3 matching products, return 3 lexicographically smallest products. These product names should be returned in lexicographical (alphabetical) order.

# Example 1:

# Input: Products: ["apple", "apricot", "application"], searchWord: "app"
# Expected Output: [["apple", "apricot", "application"], ["apple", "apricot", "application"], ["apple", "application"]]
# Justification: For the perfix 'a', "apple", "apricot", and "application" match. For the prefix 'ap', "apple", "apricot", and "application" match. For the prefix 'app', "apple", and "application" match
# Example 2:

# Input: Products: ["king", "kingdom", "kit"], searchWord: "ki"
# Expected Output: [["king", "kingdom", "kit"], ["king", "kingdom", "kit"]]
# Justification: All products starting with "k" are "king", "kingdom", and "kit". The list remains the same for the 'ki' prefix.
# Example 3:

# Input: Products: ["fantasy", "fast", "festival"], searchWord: "farm"
# Expected Output: [["fantasy", "fast", "festival"], ["fantasy", "fast"], [], []]
# Justification: Initially, "fantasy", "fast", and "festival" match 'f'. Moving to 'fa', only "fantasy" and "fast" match. No product matches with "far", and "farm".


# To solve this problem, We will use the trie data structure to store the list of products. The trie is built by inserting each product, where each node represents a character. This structure allows us to efficiently find products that share a common prefix.

# After building the trie, we process the search word by checking each of its prefixes. For each prefix, we perform a depth-first search (DFS) starting from the node matching the end of the prefix. The DFS is designed to find up to three lexicographically up to 3 smallest words that start with the given prefix. This approach of using a trie combined with DFS for each prefix ensures that we can quickly and effectively generate the required list of product suggestions.

# Input: Products = ["fantasy", "fast", "festival"], Search Word = "farm"
# Walkthrough:
# Building the Trie:
# Insert "fantasy", "fast", "festival" into the trie, creating nodes for each character.
# Mark the end of each word in the trie.
# Processing Prefixes:
# Prefix "f": Node exists. Proceed to DFS.
# Prefix "fa": Node exists. Proceed to DFS.
# Prefix "far": Node does not exist. Add an empty list to suggestions and skip DFS.
# Prefix "farm": Node does not exist. Add an empty list to suggestions and skip DFS.
# DFS for "f" and "fa":
# For "f": DFS finds "fantasy", "fast", "festival". Add these to suggestions.
# For "fa": DFS finds "fantasy", "fast". Add these to suggestions.
# Final Output:
# Suggestions: [["fantasy", "fast", "festival"], ["fantasy", "fast"], [], []].

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            # Create a new child node if the character is not already a child of the current node
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # Mark the end of a word
        node.isEnd = True
    
    def dfs(self, node, prefix, list):
        if len(list) == 3:
            return
        if node.isEnd:
            list.append(prefix)
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch in node.children:
                self.dfs(node.children[ch], prefix+ch, list)
    
    def search(self, prefix):
        node = self.root
        # Traverse the trie to the end of the prefix
        for ch in prefix:
            if ch not in node.children:
                return []  # Return an empty list if the prefix is not present
            node = node.children[ch]

        list = []
        self.dfs(node, prefix, list)  # Start DFS from the end of the current prefix
        return list
    
class Solution:
    def suggestProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        result = []
        prefix = ''
        
        for ch in searchWord:
            prefix += ch
            result.append(trie.search(prefix))
        return result

if __name__ == "__main__":
    solution = Solution()

    # Test Example 1
    products1 = ["apple", "apricot", "application"]
    searchWord1 = "app"
    print("Example 1:", solution.suggestProducts(products1, searchWord1))

    # Test Example 2
    products2 = ["king", "kingdom", "kit"]
    searchWord2 = "ki"
    print("Example 2:", solution.suggestProducts(products2, searchWord2))

    # Test Example 3
    products3 = ["fantasy", "fast", "festival"]
    searchWord3 = "farm"
    print("Example 3:", solution.suggestProducts(products3, searchWord3))


# Time Complexity
# Building the Trie: (O(N x L)), where (N) is the number of products and (L) is the average length of the products.
# Searching for Each Prefix: (O(M x K)), where (M) is the length of the search word and (K) is the time taken for the DFS, which is limited to 3 (constant time). Overall, it's approximately (O(M)).
# Overall Time Complexity: O(N * L + M), combining the time to build the Trie and perform searches.

# Space Complexity
# Trie Storage: (O(N x L)), as each product of average length (L) is stored in the trie.
# Search Results: (O(M)), as we store up to 3 suggestions for each character in the search word.
# Overall, the space complexity is dominated by the trie storage, which is (O(N x L)).