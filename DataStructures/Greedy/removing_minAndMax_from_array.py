# Determine the minimum number of deletions required to remove the smallest and the largest elements from an array of integers.

# In each deletion, you are allowed to remove either the first (leftmost) or the last (rightmost) element of the array.

# Examples
# Example 1:

# Input: [3, 2, 5, 1, 4]
# Expected Output: 3
# Justification: The smallest element is 1 and the largest is 5. Removing 4, 1, and then 5 (or 5, 4, and then 1) in three moves is the most efficient strategy.
# Example 2:

# Input: [7, 5, 6, 8, 1]
# Expected Output: 2
# Justification: Here, 1 is the smallest, and 8 is the largest. Removing 1 and then 8 in two moves is the optimal strategy.
# Example 3:

# Input: [2, 4, 10, 1, 3, 5]
# Expected Output: 4
# Justification: The smallest is 1 and the largest is 10. One strategy is to remove 2, 4, 10, and then 1 in four moves.


# To solve this problem, identify the positions of the minimum and maximum elements in the array. Then, calculate the distance of these elements from both ends of the array. The key is to find the shortest path to remove both elements, considering three scenarios: removing both from the start, both from the end, one from the start and the other from the end. The minimum number of steps among these scenarios is the answer.

class Solution:
    def minMoves(self, nums):
        n = len(nums)
        # Find the indexes of the minimum and maximum elements
        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))
        
        # Calculate distances from both ends
        minDistStart = minIndex + 1
        minDistEnd = n - minIndex
        maxDistStart = maxIndex + 1
        maxDistEnd = n - maxIndex
        
        # Determine the most efficient sequence of moves
        # Determine the most efficient sequence of moves
        totalMoves = min(
            max(minDistStart, maxDistStart),  # Both from start
            min(minDistStart + maxDistEnd, minDistEnd + maxDistStart),  # One from each end
            max(minDistEnd, maxDistEnd)  # Both from end
        )
        return totalMoves

sol = Solution()
print(sol.minMoves([3, 2, 5, 1, 4]))  # Output: 3
print(sol.minMoves([7, 5, 6, 8, 1]))  # Output: 2
print(sol.minMoves([2, 4, 10, 1, 3, 5]))  # Output: 4
