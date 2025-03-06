# Given an array of integers and an integer k, find a contiguous subarray of length k that has the highest average value, and return this maximum average value.

# Examples
# Example 1
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
# Expected Output: 5.5
# Justification: The subarray [5, 6] has the highest average (5 + 6) / 2 = 5.5.
# Example 2
# Input: nums = [0, 1, 1, 3, -1, 10, -2], k = 3
# Expected Output: 4.0
# Justification: The subarray [3, -1, 10] has the highest average (3 + (-1) + 10) / 3 = 4.0.
# Example 3
# Input: nums = [-5, -2, 0, 3, 9, -1, 2], k = 4
# Expected Output: 3.25
# Justification: The subarray [3, 9, -1, 2] has the highest average (3 + 9 + (-1) + 2) / 4 = 3.25.

# Solution
# To solve this problem, we need to find a subarray of length ( k ) with the highest average. We can use a sliding window approach to efficiently calculate the sum of subarrays. By maintaining a window of size ( k ) and sliding it across the array, we can update the sum by subtracting the element that goes out of the window and adding the new element that enters the window. This approach ensures that we only need to pass through the array once, making it efficient in terms of time complexity.

# The sliding window method is effective because it reduces the need for nested loops, which would result in higher time complexity. Instead, by adjusting the window's sum dynamically as it slides, we achieve the desired result in linear time. This makes our approach both time-efficient and easy to implement.

# Complexity Analysis
# Time Complexity: The algorithm iterates through the array once, making it O(n), where n is the number of elements in the array. This is efficient because it only requires a single pass to compute the sum of the subarrays.

# Space Complexity: The space complexity is O(1) because we are using a fixed amount of extra space regardless of the input size.


class Solution:
    def find_max_average(self, arr, k):
        n = len(arr)
        # Compute the sum of the first 'k' elements
        max_sum = sum(arr[:k])
        current_sum = max_sum
        # Slide the window across the array
        for i in range(k, n):
            current_sum += arr[i] - arr[i-k]
            max_sum = max(max_sum, current_sum)
        return max_sum/k


def main():
    sol = Solution()
    nums1 = [1, 2, 3, 4, 5, 6]
    k1 = 2
    print("Expected: 5.5, Output:", sol.find_max_average(nums1, k1))

    # Example 2
    nums2 = [0, 1, 1, 3, -1, 10, -2]
    k2 = 3
    print("Expected: 4.0, Output:", sol.find_max_average(nums2, k2))

    # Example 3
    nums3 = [-5, -2, 0, 3, 9, -1, 2]
    k3 = 4
    print("Expected: 3.25, Output:", sol.find_max_average(nums3, k3))


main()
