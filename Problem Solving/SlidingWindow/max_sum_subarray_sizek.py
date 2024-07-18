# Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

# Example 1:
# Input: arr = [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:
# Input: arr = [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# Tc: O(n) Sc: O(1)

class Solution:
    def findMaxSubArray(self, k, arr):
        maxSum, windowSum = 0, 0
        windowStart = 0
        
        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]
            if windowEnd >= k-1:
                maxSum = max(maxSum, windowSum)
                windowSum -= arr[windowStart]
                windowStart += 1
        
        return maxSum

def main():
    sol = Solution()
    print("Maximum sum of a subarray of size K: " +
        str(sol.findMaxSubArray(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
        str(sol.findMaxSubArray(2, [2, 3, 4, 1, 5])))


main()