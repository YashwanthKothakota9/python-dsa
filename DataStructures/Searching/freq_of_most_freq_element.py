# You are given an nums array containing n integers and an integer k. In a single operation, you can choose any index i and increment the nums[i] by 1.

# Return the maximum possible frequency of any element of nums after performing at most k operations.

# Example 1:

# Input: nums = [1, 2, 3], k = 3
# Expected Output: 3
# Explanation: We can increment the number 1 two times and 2 one time. The final array will be [3, 3, 3]. Now, the number 3 appears 3 times in the array [3, 3, 3].
# Example 2:

# Input: nums = [4, 4, 4, 1], k = 2
# Expected Output: 3
# Explanation: We can increment the number 1 two times (1 -> 2 -> 3). Now, the number 4 still appears 3 times, which is the maximum frequency that can be achieved with 2 operations.
# Example 3:

# Input: nums = [10, 9, 9, 4, 8], k = 5
# Expected Output: 4
# Explanation: We can increment the number 9 one time and the number 8 two times (9 -> 10, 9 -> 10; 8 -> 9 -> 10). The number 10 will then appear 4 times in the array [10, 10, 10, 4, 10].

# To solve the problem of finding the maximum frequency of an element after at most k increments using a binary search approach, we first sort the array. Sorting helps to position similar numbers next to each other, facilitating the application of binary search for efficient checking of possible solutions.

# The core idea is to use binary search to find the largest possible subarray ending at each element nums[i] that can be converted into nums[i] within the allowed operations. For each position i, we calculate the total operations needed to make all elements from an earlier position mid up to i equal to nums[i]. This calculation is done using a prefix sum array, which helps in obtaining the sum of any subarray in constant time. We adjust the search range based on whether the operations exceed k or not. This method ensures optimal time complexity as compared to a simple iterative approach.

class Solution:
    # Method to find the maximum length of subarray that can be made equal to `elements[index]` using at most `maxOperations`.
    def findMaxSubarrayLength(self, index, maxOperations, elements, cumulativeSum):
        target = elements[index]  # The target number we want to make others equal to.
        start = 0  # Start of the search range.
        end = index  # End of the search range, we consider subarrays ending at `index`.
        bestLength = index  # This will store the best start position for the longest valid subarray.
        
        while start <= end:
            mid = (start + end) // 2  # Midpoint of the current search range.
            count = index - mid + 1  # Number of elements from `mid` to `index`.
            requiredSum = count * target  # If all elements are `target`, this is the total they would sum to.
            existingSum = cumulativeSum[index] - (cumulativeSum[mid - 1] if mid > 0 else 0)  # Current sum from `mid` to `index`.
            operationsRequired = requiredSum - existingSum  # How many increments are needed to make all equal to `target`.
            
            if operationsRequired > maxOperations:
                start = mid + 1  # If more operations are required than allowed, move the start up.
            else:
                bestLength = mid  # Update bestLength as this is a valid subarray.
                end = mid - 1  # Try for a longer valid subarray.
        
        return index - bestLength + 1  # Return the length of the longest valid subarray.
    
    # Method to calculate the maximum frequency of any element after at most `maxOperations` increments.
    def maxFrequency(self, elements, maxOperations):
        elements.sort()  # Sort the array to facilitate the equalization to the highest element.
        cumulativeSum = [0] * len(elements)  # Array to store cumulative sums.
        cumulativeSum[0] = elements[0]  # Initialize the first element of cumulative sum.
        
        for i in range(1, len(elements)):
            cumulativeSum[i] = elements[i] + cumulativeSum[i - 1]  # Build the cumulative sum array.
        
        maximumFrequency = 0
        for i in range(len(elements)):
            maximumFrequency = max(maximumFrequency, self.findMaxSubarrayLength(i, maxOperations, elements, cumulativeSum))  # Compute max frequency for each end position.
        
        return maximumFrequency  # Return the maximum frequency found.

solution = Solution()
# Test cases
print("Example 1: Output:", solution.maxFrequency([1, 2, 3], 3))  # Expected output is 4
print("Example 2: Output:", solution.maxFrequency([4, 4, 4, 1], 2))  # Expected output is 3
print("Example 3: Output:", solution.maxFrequency([10, 9, 9, 4, 8], 5))  # Expected output is 3


