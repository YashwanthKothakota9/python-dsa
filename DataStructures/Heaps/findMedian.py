# As we know, the median is the middle value in an ordered integer list. So a brute force solution could be to maintain a sorted list of all numbers inserted in the class so that we can efficiently return the median whenever required. Inserting a number in a sorted list will take O(N) time if there are ‘N’ numbers in the list. This insertion will be similar to the Insertion sort. Can we do better than this? Can we utilize the fact that we don’t need the fully sorted list - we are only interested in finding the middle element?

# Assume ‘x’ is the median of a list. This means that half of the numbers in the list will be smaller than (or equal to) ‘x’ and half will be greater than (or equal to) ‘x’. This leads us to an approach where we can divide the list into two halves: one half to store all the smaller numbers (let’s call it smallNumList) and one half to store the larger numbers (let’s call it largeNumList). The median of all the numbers will either be the largest number in the smallNumList or the smallest number in the largeNumList. If the total number of elements is even, the median will be the average of these two numbers.

# The best data structure that comes to mind to find the smallest or largest number among a list of numbers is a Heap. Let’s see how we can use a heap to find a better algorithm.

# We can store the first half of numbers (i.e., smallNumList) in a Max Heap. We should use a Max Heap as we are interested in knowing the largest number in the first half.
# We can store the second half of numbers (i.e., largeNumList) in a Min Heap, as we are interested in knowing the smallest number in the second half. Inserting a number in a heap will take O(logN), which is better than the brute force approach. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.

from heapq import * # type: ignore

class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def insertNum(self,num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap,-num)
        else:
            heappush(self.minHeap,num)
            
        # either both the heaps will have equal number of elements or max-heap will have one
        # more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
        # we have even number of elements, take the average of middle two elements
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0
    

def main():
  sol = Solution()
  sol.insertNum(3)
  sol.insertNum(1)
  print("The median is: " + str(sol.findMedian()))
  sol.insertNum(5)
  print("The median is: " + str(sol.findMedian()))
  sol.insertNum(4)
  print("The median is: " + str(sol.findMedian()))


main()

# Time Complexity
# The time complexity of the insertNum() will be O(logN) due to the insertion in the heap. The time complexity of the findMedian() will be O(1) as we can find the median from the top elements of the heaps.

# Space Complexity
# The space complexity will be O(N) because, as at any time, we will be storing all the numbers.