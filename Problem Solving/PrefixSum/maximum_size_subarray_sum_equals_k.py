# Given an array of integers nums and an integer k, find the length of the longest subarray that sums to k. If no such subarray exists, return 0.
# Examples

# Example 1:

#     Input: nums = [1, 2, 3, -2, 5], k = 5
#     Output: 2
#     Explanation: The longest subarray with a sum of 5 is [2, 3], which has a length of 2.

# Example 2:

#     Input: nums = [-2, -1, 2, 1], k = 1
#     Output: 2
#     Explanation: The longest subarray with a sum of 1 is [-1, 2], which has a length of 2.

# Example 3:

#     Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
#     Output: 4
#     Explanation: The longest subarray with a sum of 7 is [7, 2, -3, 1], which has a length of 4.

# Constraints:

#     1 <= nums.length <= 2 * 105
#     -104 <= nums[i] <= 104
#     -109 <= k <= 109


# Solution

# To solve this problem, we can use a hash map (or dictionary) to keep track of the cumulative sum at each index. The key idea is to use the cumulative sum to quickly determine the length of subarrays that sum up to k. By storing the earliest occurrence of each cumulative sum, we can efficiently check if there is a subarray ending at the current index with the required sum. This approach leverages the relationship between the cumulative sums to find the longest subarray with a sum of k in linear time.

# This approach is efficient because it avoids the need for nested loops, which would result in a quadratic time complexity. Instead, by using a hash map to store the cumulative sums, we can achieve a linear time complexity, making the solution scalable for large input sizes.
# Step-by-Step Algorithm

#     Initialization:
#         Create an empty hash map (cumMap) to store cumulative sums and their earliest indices.
#         Initialize cumSum to 0 to keep track of the cumulative sum as we iterate through the array.
#         Initialize maxLen to 0 to keep track of the maximum length of the subarray with a sum of k.

#     Iterate through the array:
#         Loop through each element in the nums array using a for loop:
#             Update the cumulative sum:
#                 For each element num at index i, update the cumulative sum: cumSum += num.
#             Check if the cumulative sum equals k:
#                 If cumSum == k, update maxLen to i + 1 since the entire array from the start to the current index sums to k.
#             Check for a subarray with a sum of k:
#                 Calculate cumSum - k.
#                 If (cumSum - k) exists in cumMap, it means there is a subarray that sums to k:
#                     Update maxLen to the maximum of its current value and the length of this subarray: i - cumMap[cumSum - k].
#             Store the cumulative sum and its index:
#                 If cumSum is not already in cumMap, add it with its index i: cumMap[cumSum] = i.

#     Return the maximum length:
#         After the loop ends, return maxLen.

# Complexity Analysis

#     Time Complexity: The algorithm runs in O(N)

# time, where n is the number of elements in the array. This is because we traverse the array once and perform constant-time operations for each element.

# Space Complexity: The space complexity is O(N)

#     because, in the worst case, we may store each cumulative sum in the hash map.


class Solution:
    def max_sub_array_len(self, nums, k):
        cum_map = {}
        cum_sum = 0
        max_len = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum == k:
                max_len = i+1
            if (cum_sum - k) in cum_map:
                max_len = max(max_len, i - cum_map[cum_sum-k])
            if cum_sum not in cum_map:
                cum_map[cum_sum] = i
        return max_len


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    nums1 = [1, 2, 3, -2, 5]
    k1 = 5
    print(sol.max_sub_array_len(nums1, k1))  # Output: 2

    nums2 = [-2, -1, 2, 1]
    k2 = 1
    print(sol.max_sub_array_len(nums2, k2))  # Output: 2

    nums3 = [3, 4, 7, 2, -3, 1, 4, 2]
    k3 = 7
    print(sol.max_sub_array_len(nums3, k3))  # Output: 4
