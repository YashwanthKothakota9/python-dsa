# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

# Example 1:

# Input: nums1=[9, 8, 2], nums2=[6, 3, 1], K=3
# Output: [9, 3], [9, 6], [8, 6] 
# Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.
# Example 2:

# Input: nums1=[5, 2, 1], nums2=[2, -1], K=3
# Output: [5, 2], [5, -1], [2, 2]



# This problem follows the K-way merge pattern and we can follow a similar approach as discussed in Merge K Sorted Lists.

# We can go through all the numbers of the two input arrays to create pairs and initially insert them all in the heap until we have ‘K’ pairs in Min Heap. After that, if a pair is bigger than the top (smallest) pair in the heap, we can remove the smallest pair and insert this pair in the heap.

# We can optimize our algorithms in two ways:

# Instead of iterating over all the numbers of both arrays, we can iterate only the first ‘K’ numbers from both arrays. Since the arrays are sorted in descending order, the pairs with the maximum sum will be constituted by the first ‘K’ numbers from both the arrays.
# As soon as we encounter a pair with a sum that is smaller than the smallest (top) element of the heap, we don’t need to process the next elements of the array. Since the arrays are sorted in descending order, we won’t be able to find a pair with a higher sum moving forward.


from heapq import *

class Solution:
    def findKLargestPairs(self, nums1, nums2, k):
        minHeap = []
        for i in range(0, min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(minHeap) < k:
                    heappush(minHeap, (nums1[i]+nums2[j], i, j))
                else:
                    # if the sum of the two numbers from the two arrays is smaller than the 
                    # smallest(top) element of the heap, we can 'break' here. Since the arrays are 
                    # sorted in the descending order, we'll not be able to find a pair with a higher 
                    # sum moving forward
                    if nums1[i] + nums2[j] < minHeap[0][0]:
                        break
                    else:
                        # we've a pair with a larger sum, remove top and insert this pair in heap
                        heappop(minHeap)
                        heappush(minHeap, (nums1[i]+nums2[j], i, j))
        
        result = []
        for (num, i, j) in minHeap:
            result.append([nums1[i], nums2[j]])
        
        return result

def main():
  sol = Solution()
  print("Pairs with largest sum are: " +
        str(sol.findKLargestPairs([9, 8, 2], [6, 3, 1], 3)))


main()


# Time Complexity
# Since, at most, we’ll be going through all the elements of both arrays and we will add/remove one element in the heap in each step, the time complexity of the above algorithm will be O(NMlogK) where ‘N’ and ‘M’ are the total number of elements in both arrays, respectively.

# If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to O(K^2logK), because we are not iterating more than ‘K’ elements in both arrays.

# Space Complexity
# The space complexity will be O(K) because, at any time, our Min Heap will be storing ‘K’ largest pairs.