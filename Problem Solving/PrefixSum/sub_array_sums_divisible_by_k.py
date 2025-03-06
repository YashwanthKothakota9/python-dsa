# Given an array of integers nums and an integer k, return the count of non-empty subarrays that have a sum that is divisible by k.

# A subarray is a continuous part of an array.

# Examples
# Example 1
# Input: nums = [3, 1, 2, -2, 5, -1], k = 3
# Expected Output: 7
# Justification: The subarrays that sum to a multiple of 3 are [3], [1, 2], [3, 1, 2], [3, 1, 2, -2, 5], [1, 2, -2, 5], [-2, 5], and [2, -2].


# To solve this problem, we will use a hash map (dictionary) to keep track of the cumulative sums and their remainders when divided by k. This helps in finding the number of subarrays whose sum is divisible by k. The idea is to iterate through the array while maintaining a running sum. For each element, calculate the cumulative sum and its remainder when divided by k. If this remainder has been seen before, it indicates that there is a subarray which sum is divisible by k. By using the hash map to store and count these remainders, we efficiently count the subarrays without needing nested loops, making the approach more efficient.

# This approach works because it leverages the properties of modular arithmetic to efficiently determine subarrays that meet the criteria. Using a hash map to store the counts of remainders enables us to quickly check for existing subarrays that, when combined with the current element, form a subarray whose sum is divisible by k.


class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        cumulative_sum = 0
        count = 0
        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k
            if remainder < 0:
                remainder += k
            count += remainder_count.get(remainder, 0)
            remainder_count[remainder] = remainder_count.get(remainder, 0)+1
        return count


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [3, 1, 2, -2, 5, -1]
    k1 = 3
    print(solution.subarraysDivByK(nums1, k1))  # 7

    # Example 2
    nums2 = [4, 5, 0, -2, -3, 1]
    k2 = 5
    print(solution.subarraysDivByK(nums2, k2))  # 7

    # Example 3
    nums3 = [-1, 2, 9]
    k3 = 2
    print(solution.subarraysDivByK(nums3, k3))  # 2


# Complexity Analysis
# Time Complexity
# The time complexity of the algorithm is O(n), where (n) is the number of elements in the input array nums. This is because we traverse the array exactly once, performing constant-time operations for each element.

# Space Complexity
# The space complexity of the algorithm is O(k), where (k) is the value of the divisor. This is due to the hash map (or dictionary) that stores at most (k) different remainders. In the worst case, the hash map will store all possible remainders from (0) to (k-1).
