# Given an integer array nums sorted in increasing order, return an array result of the same length, where result[i] should be the sum of the absolute differences between nums[i] and every other element in nums.

# Example 1
# Input: [1, 3, 6]
# Output: [7, 5, 8]
# Explanation:
# For result[0]: |1-3| + |1-6| = 2 + 5 = 7
# For result[1]: |3-1| + |3-6| = 2 + 3 = 5
# For result[2]: |6-1| + |6-3| = 5 + 3 = 8


# Example 2
# Input: [2, 4, 7]
# Output: [7, 5, 8]
# Explanation:
# For result[0]: |2-4| + |2-7| = 2 + 5 = 7
# For result[1]: |4-2| + |4-7| = 2 + 3 = 5
# For result[2]: |7-2| + |7-4| = 5 + 3 = 8


# Solution
# To solve this problem, we need to calculate the sum of absolute differences for each element in the array. We can simplify this by using prefix sums to avoid repeatedly calculating the same differences. By leveraging prefix sums, we can compute the total difference more efficiently.

# For each element, we will split the array into two parts: the left part and the right part. The left part includes all elements before the current one, and the right part includes all elements after the current one. Using the prefix sums, we can quickly get the sum of elements on the left and right, then use these sums to calculate the absolute differences. This method avoids the need for nested loops and reduces the time complexity.


class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        result = [0]*n
        prefix_sum = [0]*(n+1)

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(n):
            lef_sum = prefix_sum[i]
            right_sum = prefix_sum[n] - prefix_sum[i+1]
            result[i] = i*nums[i] - lef_sum + right_sum - (n-i-1)*nums[i]
        return result


if __name__ == "__main__":
    sol = Solution()
    example1 = [1, 3, 6]
    example2 = [2, 4, 7]
    example3 = [1, 2, 4, 5]

    print(sol.getSumAbsoluteDifferences(example1))  # [7, 5, 8]
    print(sol.getSumAbsoluteDifferences(example2))  # [7, 5, 8]
    print(sol.getSumAbsoluteDifferences(example3))  # [8, 6, 6, 8]


# Complexity Analysis
# Time Complexity
# Prefix Sum Calculation: We iterate through the array once to calculate the prefix sums, which takes O(n) time.
# Result Calculation: We iterate through the array once more to compute the result for each element, which also takes O(n) time.
# Thus, the overall time complexity is O(n), where n is the length of the input array.

# Space Complexity
# We use an extra array of size n+1 for the prefix sums.
# We also use an extra array of size n for the result.
# Thus, the overall space complexity is O(n).
