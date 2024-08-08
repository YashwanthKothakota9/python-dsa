# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

# Example 1:

# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:

# [1, 2, -1, 3, 5] -> median is 1.5
# [1, 2, -1, 3, 5] -> median is 0.5
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 4.0

# Example 2:

# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Let's consider all windows of size ‘3’:

# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 2.0
# [1, 2, -1, 3, 5] -> median is 3.0

from heapq import *
import heapq

class Solution:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def findSlidingWindowMedian(self, nums, k):
        result = []
        for i in range(len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i >= k - 1:
                if len(self.maxHeap) == len(self.minHeap):
                    result.append((-self.maxHeap[0] + self.minHeap[0]) / 2.0)
                else:
                    result.append(-self.maxHeap[0])

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        heap.pop()
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

def main():
    sol = Solution()
    result = sol.findSlidingWindowMedian([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are:", result)

    sol = Solution()
    result = sol.findSlidingWindowMedian([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are:", result)

if __name__ == "__main__":
    main()


# Time Complexity
# The time complexity of our algorithm is O(N*K) where ‘N’ is the total number of elements in the input array and ‘K’ is the size of the sliding window. This is due to the fact that we are going through all the ‘N’ numbers and, while doing so, we are doing two things:

# Inserting/removing numbers from heaps of size ‘K’. This will take O(logK).
# Removing the element going out of the sliding window. This will take O(K) as we will be searching this element in an array of size ‘K’ (i.e., a heap).
# Space Complexity
# Ignoring the space needed for the output array, the space complexity will be O(K) because, at any time, we will be storing all the numbers within the sliding window.