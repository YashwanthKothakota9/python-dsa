# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

# Let's understand this problem with an example:

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Here, we are asked to find the average of all subarrays of '5' contiguous elements in the given array. Let's solve this:

# For the first 5 numbers (subarray from index 0-4), the average is:
# The average of next 5 numbers (subarray from index 1-5) is:
# For the next 5 numbers (subarray from index 2-6), the average is:
# ...
# Here is the final output containing the averages of all subarrays of size 5:

# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

# TC: O(N)
# SC: O(N)


class Solution:
    def find_averages(self, K, arr):
        result = []
        window_sum, window_start = 0.0, 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            # slide the window, no need to slide if we've not hit the required window size of 'k'
            if window_end >= K-1:
                result.append(window_sum/K)
                window_sum -= arr[window_start]
                window_start += 1
        return result


def main():
    sol = Solution()
    result = sol.find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
