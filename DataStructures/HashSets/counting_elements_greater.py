# Given a list of integers, determine the count of numbers for which there exists another number in the list that is greater by exactly one unit.

# In other words, for each number x in the list, if x + 1 also exists in the list, then x is considered for the count.

# Examples:

# Example 1:

# Input: [4, 3, 1, 5, 6]
# Expected Output: 3
# Justification: The numbers 4, 3, and 5 have 5, 4, and 6 respectively in the list, which are greater by exactly one unit.
# Example 2:

# Input: [7, 8, 9, 10]
# Expected Output: 3
# Justification: The numbers 7, 8, and 9 have 8, 9, and 10 respectively in the list, which are greater by exactly one unit.
# Example 3:

# Input: [11, 13, 15, 16]
# Expected Output: 1
# Justification: Only the number 15 has 16 in the list, which is greater by exactly one unit.

from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_set = set(arr)
        count = 0
        for num in arr:
            if num+1 in num_set:
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.countElements([4, 3, 1, 5, 6]))  # Expected: 3
    print(sol.countElements([7, 8, 9, 10]))   # Expected: 3
    print(sol.countElements([11, 13, 15, 16])) # Expected: 1