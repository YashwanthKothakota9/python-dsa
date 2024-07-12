# Given a collection of pairs where each pair contains two elements [a, b], find the maximum length of a chain you can form using pairs.

# A pair [a, b] can follow another pair [c, d] in the chain if b < c.

# You can select pairs in any order and don't need to use all the given pairs.

# Examples
# Example 1:

# Input: [[1,2], [3,4], [2,3]]
# Expected Output: 2
# Justification: The longest chain is [1,2] -> [3,4]. The chain [1,2] -> [2,3] is invalid because 2 is not smaller than 2.
# Example 2:

# Input: [[5,6], [1,2], [8,9], [2,3]]
# Expected Output: 3
# Justification: The chain can be [1,2] -> [5,6] -> [8,9] or [2,3] -> [5,6] -> [8, 9].
# Example 3:

# Input: [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]
# Expected Output: 3
# Justification: The longest possible chain is formed by chaining [1,2] -> [3,5] -> [7,8].


# The greedy approach to solving the problem involves initially sorting the pairs based on their second elements. This step is crucial as it aligns the pairs in a way that the one with the smallest end is considered first, leading to more opportunities for chain extension.

# After sorting, we iterate through the pairs, maintaining a variable to track the current end of the chain. For each pair, if the first element is greater than the current chain end, we extend the chain by adding this pair and updating the chain end to this pair's second element. This method ensures that at each step, we're making the most optimal choice to extend the chain without needing to consider previous pairs, thereby maximizing the number of pairs in the chain with the least end values first, leading to the longest possible chain.

class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x:x[1])
        
        currentEnd = float('-inf')
        chainCount = 0
        
        for pair in pairs:
            if pair[0] > currentEnd:
                currentEnd = pair[1]
                chainCount += 1
        return chainCount

solution = Solution()
example1 = [[1,2], [3,4], [2,3]]
example2 = [[5,6], [1,2], [8,9], [2,3]]
example3 = [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]

print("Example 1:", solution.findLongestChain(example1))  # Expected Output: 2
print("Example 2:", solution.findLongestChain(example2))  # Expected Output: 3
print("Example 3:", solution.findLongestChain(example3))  # Expected Output: 3