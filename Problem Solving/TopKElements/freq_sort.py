# Given a string, sort it based on the decreasing frequency of its characters.

# Example 1:

# Input: "Programming"
# Output: "rrggmmPiano"
# Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
# Example 2:

# Input: "abcbab"
# Output: "bbbaac"
# Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.


# This problem follows the Top ‘K’ Elements pattern, and shares similarities with Top ‘K’ Frequent Numbers.

# We can follow the same approach as discussed in the Top ‘K’ Frequent Numbers problem. First, we will find the frequencies of all characters, then use a max-heap to find the most occurring characters.

from heapq import * #type:ignore

class Solution:
    def sortCharByFreq(self, s:str):
        # find the frequency of each character
        charFreqMap = {}
        for char in s:
            charFreqMap[char] = charFreqMap.get(char, 0)+1
        
        maxHeap = []
        # add all characters to the max heap
        for char, freq in charFreqMap.items():
            heappush(maxHeap, (-freq, char))
        
        print(f"MaxHeap: {maxHeap}")
        
        # build a string, appending the most occurring characters first
        sortedString = []
        while maxHeap:
            freq, char = heappop(maxHeap)
            for _ in range(-freq):
                sortedString.append(char)
        
        return ''.join(sortedString)

def main():
  sol = Solution()
  print("String after sorting characters by frequency: " +
        sol.sortCharByFreq("Programming"))
  print("String after sorting characters by frequency: " +
        sol.sortCharByFreq("abcbab"))


main()


# Time Complexity
# The time complexity of the above algorithm is O(D∗logD) where ‘D’ is the number of distinct characters in the input string. This means, in the worst case, when all characters are unique the time complexity of the algorithm will be O(N∗logN) where ‘N’ is the total number of characters in the string.

# Space Complexity
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.


