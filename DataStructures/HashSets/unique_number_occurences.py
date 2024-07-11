# Given an array of integers, determine if the number of times each distinct integer appears in the array is unique.

# In other words, the occurrences of each integer in the array should be distinct from the occurrences of every other integer.

# Examples:

# Input: [4, 5, 4, 6, 6, 6]
# Expected Output: true
# Justification: The number 4 appears 2 times, 5 appears 1 time, and 6 appears 3 times. All these occurrences (1, 2, 3) are unique.
# Input: [7, 8, 8, 9, 9, 9, 10, 10]
# Expected Output: false
# Justification: The number 7 appears 1 time, 8 appears 2 times, 9 appears 3 times, and 10 appears 2 times. The occurrences are not unique since the number 2 appears twice.
# Input: [11, 12, 13, 14, 14, 15, 15, 15]
# Expected Output: false
# Justification: The number 11 appears 1 time, 12 appears 1 time, 13 appears 1 time, 14 appears 2 times, and 15 appears 3 times. These occurrences are not unique.

from collections import Counter

class Solution:
    def uniqueOccurences(self, arr):
        countMap = Counter(arr)
        print(countMap)
        uniqueCounts = set()
        for count in countMap.values():
            if count in uniqueCounts:
                return False
            uniqueCounts.add(count)
        return True
    
sol = Solution()
print(sol.uniqueOccurences([4, 5, 4, 6, 6, 6]))
print(sol.uniqueOccurences([7, 8, 8, 9, 9, 9, 10, 10]))
print(sol.uniqueOccurences([11, 12, 13, 14, 14, 15, 15, 15]))
