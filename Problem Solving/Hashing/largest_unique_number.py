# Given an array of integers, identify the highest value that appears only once in the array. If no such number exists, return -1.

# Examples:

# Example 1:

# Input: [5, 7, 3, 7, 5, 8]
# Expected Output: 8
# Justification: The number 8 is the highest value that appears only once in the array.
# Example 2:

# Input: [1, 2, 3, 2, 1, 4, 4]
# Expected Output: 3
# Justification: The number 3 is the highest value that appears only once in the array.
# Example 3:

# Input: [9, 9, 8, 8, 7, 7]
# Expected Output: -1
# Justification: There is no number in the array that appears only once.


# To solve this problem, we utilize a hashmap to track the frequency of each number in the given array. The key idea is to iterate through the array, recording the count of each number in the hashmap. Once all elements are accounted for, we scan through the hashmap, focusing on elements with a frequency of one. Among these, we identify the maximum value. This approach ensures that we effectively identify the largest number that appears exactly once in the array, leveraging the hashmap for efficient frequency tracking and retrieval.


from collections import defaultdict
from typing import List

class Solution:
    def largestUniqNum(self, A: List[int]) -> int:
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        maxUnique = -1
        for key, value in freq.items():
            if value == 1:
                maxUnique = max(maxUnique, key)
        return maxUnique


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestUniqNum([5, 7, 3, 7, 5, 8]))  # Expected: 8
    print(sol.largestUniqNum([1, 2, 3, 2, 1, 4, 4]))  # Expected: 3
    print(sol.largestUniqNum([9, 9, 8, 8, 7, 7]))   # Expected: -1

# Tc: O(n) Sc: O(n)