# Given an array nums having an n elements, identify the element that appears the majority of the time, meaning more than n/2 times.

# Examples
# Example 1:

# Input: [1, 2, 2, 3, 2]
# Expected Output: 2
# Justification: Here, '2' appears 3 times in a 5-element array, making it the majority element.
# Example 2:

# Input: [4, 4, 4, 4, 7, 4, 4]
# Expected Output: 4
# Justification: '4' is the majority element as it appears 5 out of 7 times.
# Example 3:

# Input: [9, 9, 1, 1, 9, 1, 9, 9]
# Expected Output: 9
# Justification: '9' is the majority element, appearing 5 times in an 8-element array.

# The divide and conquer algorithm can be used to find the majority element in an array efficiently. The strategy involves recursively dividing the array into two halves until each segment contains a single element. At this base level, a single element is trivially the majority of its one-element segment. As we merge these segments back together, we determine the majority element of each merged segment by comparing the counts of the majority elements from the two halves. The majority element of the entire array is the one that remains the majority as segments are progressively merged.

class Solution:
    def findMajority(self, arr):
        
        def majorityRec(start, end):
            if start == end:
                return arr[start]
            
            mid = start + (end - start) // 2
            
            leftMajority = majorityRec(start, mid)
            rightMajority = majorityRec(mid+1, end)
            
            if leftMajority == rightMajority:
                return leftMajority
            
            leftCount = arr[start:end+1].count(leftMajority)
            rightCount = arr[start:end+1].count(rightMajority)
            
            return leftMajority if leftCount > rightCount else rightMajority
        
        return majorityRec(0, len(arr)-1)

sol = Solution()
print(sol.findMajority([1, 2, 2, 3, 2])) # Expect 2
print(sol.findMajority([4, 4, 4, 4, 7, 4, 4])) # Expect 4
print(sol.findMajority([9, 9, 1, 1, 9, 1, 9, 9])) # Expect 9
