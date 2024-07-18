# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

# Example 1:

# Input: arr = [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Example 2:

# Input: arr = [2, 1, 5, 2, 8], S=7
# Output: 1 
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: arr = [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

# To solve this problem, we use a sliding window approach. This technique involves expanding and contracting a window over the array to find the shortest subarray that meets the condition. By keeping a running sum of the elements in the window, we can check if the current window meets or exceeds the target sum S. If it does, we try to shrink the window from the left to see if we can get a smaller subarray that still meets the requirement. This approach is efficient because it processes each element of the array only once, resulting in a linear time complexity.

# The sliding window approach is effective because it avoids the need for nested loops, which would result in higher time complexity. By dynamically adjusting the window size, we can efficiently find the smallest subarray that meets the condition without re-evaluating the sum for different subarrays multiple times.

# Tc: O(N) Sc: O(1)

import math

class Solution:
    def findMinSubArray(self, s, arr):
        window_sum = 0
        min_length = math.inf
        window_start = 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1
        
        if min_length == math.inf:
            return 0
        return min_length

def main():
    sol = Solution()
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(8, [3, 4, 1, 1, 6])))

main()