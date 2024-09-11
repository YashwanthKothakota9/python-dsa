# Given a list of distinct strings products and a string searchWord.

# Determine a set of product suggestions after each character of the search word is typed. Every time a character is typed, return a list containing up to three product names from the products list that have the same prefix as the typed string.

# If there are more than 3 matching products, return 3 lexicographically smallest products. These product names should be returned in lexicographical (alphabetical) order.


# Examples
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

# Step-by-Step Algorithm
# Build the Trie:

# Create a root node representing the starting point of the trie.
# For each product:
# Start from the root and for each character in the product, navigate to the corresponding child node. Create a new node if it doesn't exist.
# Mark the node corresponding to the last character of the product as a word end.
# Process Each Prefix of the Search Word:

# Initialize an empty list to store the final suggestions for each prefix.
# For each character in the search word, form a prefix.
# Start from the root of the trie and navigate to the node corresponding to the last character of the current prefix.
# If the node for the current prefix doesn't exist, add an empty list to the suggestions and move to the next prefix.
# DFS for Each Prefix:

# Upon reaching the node corresponding to the current prefix, perform a DFS.
# Initialize an empty buffer to store up to three products.
# Explore all possible paths from the current node. If a path leads to a node marked as a word end, add the corresponding product to the buffer.
# Stop the DFS when you have collected three products or explored all paths.
# Compile Suggestions:

# Add the buffer containing up to three products to the list of suggestions for the current prefix.
# Continue the process for the next prefix.

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
        # Stop if we already have 3 suggestions
        if len(list) == 3:
            return
        # Add the word to the list if we're at the end of a word
        if node.isEnd:
            list.append(prefix)

        # Recursively search for all possible words
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch in node.children:
                self.dfs(node.children[ch], prefix + ch, list)

    def search(self, prefix):
        node = self.root
        # Traverse the trie to the end of the prefix
        for ch in prefix:
            if ch not in node.children:
                return []  # Return an empty list if the prefix is not present
            node = node.children[ch]

        list = []
        # Start DFS from the end of the current prefix
        self.dfs(node, prefix, list)
        return list


class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        # Insert each product into the trie
        for product in products:
            trie.insert(product)

        result = []
        prefix = ''
        # For each character in the search word, find the top 3 suggestions
        for ch in searchWord:
            prefix += ch
            result.append(trie.search(prefix))
        return result


if __name__ == "__main__":
    solution = Solution()

    # Test Example 1
    products1 = ["apple", "apricot", "application"]
    searchWord1 = "app"
    print("Example 1:", solution.suggestedProducts(products1, searchWord1))

    # Test Example 2
    products2 = ["king", "kingdom", "kit"]
    searchWord2 = "ki"
    print("Example 2:", solution.suggestedProducts(products2, searchWord2))

    # Test Example 3
    products3 = ["fantasy", "fast", "festival"]
    searchWord3 = "farm"
    print("Example 3:", solution.suggestedProducts(products3, searchWord3))


# Time Complexity
# Building the Trie: (O(N x L)), where (N) is the number of products and (L) is the average length of the products.
# Searching for Each Prefix: (O(M x K)), where (M) is the length of the search word and (K) is the time taken for the DFS, which is limited to 3 (constant time). Overall, it's approximately (O(M)).
# Overall Time Complexity: O(N * L + M), combining the time to build the Trie and perform searches.

# Space Complexity
# Trie Storage: (O(N x L)), as each product of average length (L) is stored in the trie.
# Search Results: (O(M)), as we store up to 3 suggestions for each character in the search word.
# Overall, the space complexity is dominated by the trie storage, which is (O(N x L)).
