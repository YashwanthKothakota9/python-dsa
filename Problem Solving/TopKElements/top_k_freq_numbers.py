# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example 1:

# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.
# Example 2:

# Input: [5, 12, 11, 3, 11], K = 2
# Output: [11, 5] or [11, 12] or [11, 3]
# Explanation: Only '11' appeared twice, all other numbers appeared once.

# This problem follows Top ‘K’ Numbers. The only difference is that in this problem, we need to find the most frequently occurring number compared to finding the largest numbers.

# We can follow the same approach as discussed in the Top K Elements problem. However, in this problem, we first need to know the frequency of each number, for which we can use a HashMap. Once we have the frequency map, we can use a Min Heap to find the ‘K’ most frequently occurring number. In the Min Heap, instead of comparing numbers we will compare their frequencies in order to get frequently occurring numbers

from heapq import * # type: ignore

class Solution:
    def findTopKFreqNumbers(self, nums, k):
        # find the frequency of each number
        numFreqMap = {}
        for num in nums:
            numFreqMap[num] = numFreqMap.get(num, 0)+1
        
        minHeap = []
        
        # go through all numbers of the numFrequencyMap and push them in the minHeap, which 
        # will have top k frequent numbers. If the heap size is more than k, we remove the 
        # smallest(top) number
        for num, freq in numFreqMap.items():
            print(f"minHeap: {minHeap}")
            heappush(minHeap, (freq, num))
            print(f"minHeap: {minHeap}")
            if len(minHeap) > k:
                heappop(minHeap)
            print(f"minHeap: {minHeap}")
        
        # create a list of top k numbers
        topNumbers = []
        while minHeap:
            topNumbers.append(heappop(minHeap)[1])
        
        return topNumbers

def main():
  sol = Solution()
  print("Here are the K frequent numbers: " +
        str(sol.findTopKFreqNumbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(sol.findTopKFreqNumbers([5, 12, 11, 3, 11], 2)))


main()


# Time Complexity
# The time complexity of the above algorithm is O(N+N*logK).

# Space Complexity
# The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap. For the frequency map, however, we need to store all the ‘N’ numbers.