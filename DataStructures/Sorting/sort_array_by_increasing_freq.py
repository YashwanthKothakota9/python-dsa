# Given an array nums containing the integers, return the resultant array after sorting it in increasing order based on the frequency of the values. If two numbers have the same frequency, they should be sorted in descending numerical order.

# Examples
# Example 1:

# Input: nums = [4, 4, 6, 2, 2, 2]
# ExpectedOutput: [6, 4, 4, 2, 2, 2]
# Justification: Here, '6' appears once, '4' appears twice, and '2' appears three times. Thus, numbers are first sorted by frequency and then by value when frequencies tie.
# Example 2:

# Input: nums = [0, -1, -1, -1, 5]
# ExpectedOutput: [5, 0, -1, -1, -1]
# Justification: '5' and '0' appears once, and '-1' appears three times. After sorting by frequency and resolving ties by sorting in descending order, the result is obtained.
# Example 3:

# Input: nums = [10, 10, 10, 20, 20, 30]
# ExpectedOutput: [30, 20, 20, 10, 10, 10]
# Justification: Here, '30' has the lowest frequency, followed by '20', and '10' has the highest frequency. They are sorted accordingly.

class Solution:
    
    def freqSort(self, nums):
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1
        self.mergeSort(nums, 0, len(nums)-1, freqMap)
        return nums
    
    def mergeSort(self, nums, left, right, freqMap):
        if left < right:
            mid = ( left + right )//2
            self.mergeSort(nums,left,mid,freqMap)
            self.mergeSort(nums,mid+1,right,freqMap)
            self.merge(nums,left,mid,right,freqMap)
    
    def merge(self, nums, left, mid, right, freqMap):
        leftArray = nums[left : mid+1]
        rightArray = nums[mid + 1: right]
        
        i,j,k = 0,0,left
        while i < len(leftArray) and j < len(rightArray):
            if freqMap[leftArray[i]] < freqMap[rightArray[j]] or freqMap[leftArray[i]] == freqMap[rightArray[j]] and leftArray[i] > rightArray[j]:
                nums[k] = leftArray[i]
                i += 1
            else:
                nums[k] = rightArray[j]
                j += 1
            k += 1
        
        while i<len(leftArray):
            nums[k] = leftArray[i]
            i += 1
            k += 1
        
        while j < len(rightArray):
            nums[k] = rightArray[j]
            j += 1
            k += 1

sol = Solution()

# Test Cases
nums1 = [4, 4, 6, 2, 2, 2]
print("Example 1:", sol.freqSort(nums1))  # [6, 4, 4, 2, 2, 2]

nums2 = [0, -1, -1, -1, 5]
print("Example 2:", sol.freqSort(nums2))  # [5, 0, -1, -1, -1]

nums3 = [10, 10, 10, 20, 20, 30]
print("Example 3:", sol.freqSort(nums3))  # [30, 20, 20, 10, 10, 10]
