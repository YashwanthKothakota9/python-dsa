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

# Sorting the Pairs: Initially, sort all pairs based on their second element in ascending order. This ensures that as you iterate through the pairs, you are always considering the pair with the next smallest endpoint.

# Initializing Variables: Start with two variables: one to keep track of the current endpoint of the chain (currentEnd) and another to count the number of pairs in the chain (chainCount). Initialize currentEnd to the lowest possible value (e.g., Integer.MIN_VALUE) and chainCount to 0.

# Iterating and Choosing Pairs: Iterate through the sorted pairs. For each pair, check if its first element is greater than currentEnd. If it is, it means this pair can be appended to the current chain. Update currentEnd to the second element of this pair and increment chainCount.

# Result: After iterating through all pairs, chainCount will hold the maximum number of pairs that can be chained.

# This Greedy approach is effective because it always chooses the option that seems best at the moment (the pair with the smallest endpoint) and this local optimal choice leads to a globally optimal solution in this specific problem context. The logic behind this is that by choosing the pair with the smallest endpoint, you are maximizing the potential for other pairs to be chained afterward.

# Input Pairs: [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]

# After Sorting by Second Element: [[1,2], [2,3], [3,5], [4,5], [5,6], [7,8]]

# Iterating through Pairs:

# Start with currentEnd = Integer.MIN_VALUE and chainCount = 0.
# Pair [1,2]: 1 > Integer.MIN_VALUE. Update currentEnd to 2, chainCount to 1.
# Pair [2,3]: 2 > 2 is false. Skip.
# Pair [3,5]: 3 > 2. Update currentEnd to 5, chainCount to 2.
# Pair [4,5]: 4 > 5 is false. Skip.
# Pair [5,6]: 5 > 5 is false. Skip.
# Pair [7,8]: 7 > 5. Update currentEnd to 8, chainCount to 3.
# Result: chainCount = 3 indicates the maximum number of pairs that can be chained.

class Solution:
    def findLongestChain(self, pairs):
        # Sort pairs based on their second element in ascending order
        pairs.sort(key = lambda x:x[1])
        
        currEnd = float('-inf')
        chainCount = 0
        
        # Iterate through the sorted pairs
        for pair in pairs:
            # Check if the first element of the pair is greater than the current end
            if pair[0] > currEnd:
                currEnd = pair[1]
                chainCount += 1
        
        return chainCount

solution = Solution()
example1 = [[1,2], [3,4], [2,3]]
example2 = [[5,6], [1,2], [8,9], [2,3]]
example3 = [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]

print("Example 1:", solution.findLongestChain(example1))  # Expected Output: 2
print("Example 2:", solution.findLongestChain(example2))  # Expected Output: 3
print("Example 3:", solution.findLongestChain(example3))  # Expected Output: 3


# Time Complexity: The code takes (O(n log n)) time to run, mainly due to sorting the input pairs.

# Space Complexity: It uses (O(n)) additional space due to the input array of pairs.