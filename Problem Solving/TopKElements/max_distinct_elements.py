# Given an array of numbers nums and an integer K, find the maximum number of distinct elements after removing exactly K elements from the nums array.

# Example 1:

# Input: nums = [7, 3, 5, 8, 5, 3, 3], K=2
# Expected Output: 3
# Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have to skip 5 because it is not distinct and occurred twice. Another solution could be to remove one instance of '5' and '3' each to be left with three distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.
# Example 2:

# Input: [3, 5, 12, 11, 12], and K=3
# Expected Output: 2
# Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then we can delete any two numbers which will leave us 2 distinct numbers in the result.
# Example 3:

# Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
# Expected Output: 3
# Explanation: We can remove one occurrence of '4' to get three distinct numbers 1, 2 and 4.


# This problem follows the Top ‘K’ Numbers pattern, and shares similarities with Top ‘K’ Frequent Numbers.

# To solve this problem, we need to determine the maximum number of distinct elements that can be left in the array after removing k elements. The core idea is to prioritize the removal of elements with higher frequencies first, as this will maximize the number of distinct elements remaining. By reducing the frequency of these elements, we can potentially convert them into distinct elements.

# The algorithm starts by calculating the frequency of each element in the array. Then, we use a min-heap (priority queue) to store elements based on their frequencies in ascending order. This allows us to efficiently access and remove the least frequent elements first. For each element in the min-heap, we reduce its frequency by removing occurrences until either all occurrences are removed or k elements have been removed. Finally, if there are any removals left (k > 0), we decrement the count of distinct elements accordingly.

# Step-by-Step Algorithm
# Initialize Frequency Map:

# Create a map to store the frequency of each element in the array.
# Iterate through the array, updating the frequency of each element in the map.
# Create Min-Heap:

# Initialize a min-heap (priority queue) to store elements based on their frequency.
# Iterate through the frequency map:
# If an element's frequency is 1, increment the count of distinct elements.
# If an element's frequency is greater than 1, add it to the min-heap.
# Remove Elements:

# While k is greater than 0 and the min-heap is not empty:
# Extract the element with the lowest frequency from the heap.
# Calculate the number of occurrences to be removed (frequency - 1).
# Decrement k by this number.
# If k is non-negative, increment the count of distinct elements.
# Adjust Distinct Count:

# If k is still greater than 0 after processing the min-heap, decrement the count of distinct elements by k. It removes remaining elements from the distinct elements.
# Return Result:

# Return the count of distinct elements.


from heapq import *

class Solution:
    def findMaximumDistinctElements(self, nums, k):
        distinctElementsCount = 0
        
        # find the frequency of each number
        numFreqMap = {}
        for i in nums:
            numFreqMap[i] = numFreqMap.get(i,0) + 1
        
        minHeap = []
        # insert all numbers with frequency greater than '1' into the min-heap
        for num, freq in numFreqMap.items():
            if freq == 1:
                distinctElementsCount += 1
            else:
                heappush(minHeap, (freq, num))
        
        # following a greedy approach, try removing the least frequent numbers first from 
        # the min-heap
        while k > 0 and minHeap:
            freq, num = heappop(minHeap)
            # to make an element distinct, we need to remove all of its occurrences except one
            k -= freq - 1
            if k >= 0:
                distinctElementsCount += 1
        
        # if k > 0, this means we have to remove some distinct numbers
        if k > 0:
            distinctElementsCount -= k
        
        return distinctElementsCount

def main():
  sol = Solution()
  print("Maximum distinct numbers after removing K numbers: " +
        str(sol.findMaximumDistinctElements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(sol.findMaximumDistinctElements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(sol.findMaximumDistinctElements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()

# Time Complexity
# Frequency Map Construction: Building the frequency map requires iterating through the array, which takes O(N) time, where (N) is the number of elements in the array.

# Min-Heap Construction: Inserting elements into the min-heap based on their frequencies. Each insertion operation into the heap takes O(NlogN) time.

# Removing Elements: Removing elements from the min-heap and updating the count takes O(KlogN) time, where (K) is the number of elements to remove. This is because each removal operation from the heap takes O(logN) time, and in the worst case, we might remove (K) elements.

# Therefore, the overall time complexity is: O(N)+O(NlogN)+O(KlogN) Since (K) can be at most (N), this simplifies to: O(NlogN)

# Space Complexity
# Frequency Map: The space required to store the frequency map is O(N) since, in the worst case, each element in the array is distinct.

# Min-Heap: The space required to store the elements in the min-heap is O(N) since, in the worst case, all elements might be inserted into the heap.

# Therefore, the overall space complexity is: O(N)+O(N)=O(N)