# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example 1:

# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.
# Example 2:

# Input: [5, 12, 11, 3, 11], K = 2
# Output: [11, 5] or [11, 12] or [11, 3]
# Explanation: Only '11' appeared twice, all other numbers appeared once.


from heapq import * # type: ignore

class Solution:
    def findTopKFreqNumbers(self, nums, k):
        numFreqMap = {}
        for num in nums:
            numFreqMap[num] = numFreqMap.get(num, 0) + 1
        
        minHeap = []
        # go through all numbers of the numFrequencyMap and push them in the minHeap, which 
        # will have top k frequent numbers. If the heap size is more than k, we remove the 
        # smallest(top) number
        for num, freq in numFreqMap.items():
            heappush(minHeap, (freq,num))
            if len(minHeap) > k:
                heappop(minHeap)
        
        # create a list of top k numbers
        topNums = []
        while minHeap:
            topNums.append(heappop(minHeap)[1])

        return topNums

def main():
  sol = Solution()
  print("Here are the K frequent numbers: " +
        str(sol.findTopKFreqNumbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(sol.findTopKFreqNumbers([5, 12, 11, 3, 11], 2)))


main()