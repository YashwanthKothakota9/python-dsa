# Given a binary called nums and an integer called goal, return the number of subarrays that have a sum equal to goal.

# A subarray is a part of the array that is continuous, meaning all its elements are next to each other.
# Examples
# Example 1

# Input: nums = [1, 1, 0, 1, 1], goal = 2
# Expected Output: 5
# Justification: The subarrays with a sum of 3 are: [1, 1](from index 0 to 1), [1, 1, 0](from index 0 to 2), [1, 0, 1](from index 1 to 3), [0, 1, 1](from index 2 to 5), and [1, 1](from index 4 to 5).

# Example 2

# Input: nums = [1, 1, 1, 1, 0, 0], goal = 3
# Expected Output: 4
# Justification: The subarrays with a sum of 3 are: [1, 1, 1](from index 0 to 2), [1, 1, 1](from index 1 to 3), [1, 1, 1, 0](from index 1 to 4), and [1, 1, 1, 0, 0](from index 1 to 5).

# Example 3

# Input: nums = [0, 0, 0, 0, 1, 0, 1], goal = 1
# Expected Output: 12
# Justification: The subarrays with a sum of 1 are: [0, 0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1], [0, 1], [1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0], [1, 0], [0, 1], and [1]`.

# Solution

# To solve this problem, we can use a technique called the prefix sum combined with a hashmap ( or dictionary). The prefix sum helps in calculating the sum of elements in any subarray efficiently. We will keep a running total (prefix sum) as we iterate through the array. For each prefix sum, we will check if there is a previous prefix sum that, when subtracted from the current prefix sum, equals the goal. This way, we can count the subarrays that meet the requirement.

# This approach works because it allows us to find the subarray sums in constant time by leveraging previously computed sums stored in the hashmap. This is efficient and avoids the need for a nested loop, reducing the time complexity from O(n ^ 2) to O(n).

# Step-by-step Algorithm

# Initialize a variable count to 0. This will hold the number of subarrays that sum up to the goal.
# Initialize a variable prefix_sum to 0. This will keep track of the sum of elements from the start up to the current position.
# Initialize a hashmap(dictionary) prefix_sums with one entry {0: 1}. This accounts for subarrays that start from the beginning.
# Iterate through each element in the array nums.
# Add the current element to prefix_sum.
# Check if prefix_sum - goal exists in the prefix_sums. If it does, add the value of prefix_sums[prefix_sum - goal] to count.
# Increment the value of prefix_sum in prefix_sums by 1. If prefix_sum is not in the hashmap, set it to 1.
# After the loop, count will hold the number of subarrays with a sum equal to goal.

# Algorithm Walkthrough

# Using the input nums = [1, 1, 0, 1, 1] and goal = 2:

#     Initialize count = 0, prefix_sum = 0, prefix_sums = {0: 1}
#     Iterate through nums:
#         Step 1: Current element 1
#             prefix_sum = 1
#             prefix_sum - goal = -1 (not in prefix_sums)
#             Update prefix_sums: {0: 1, 1: 1}
#         Step 2: Current element 1
#             prefix_sum = 2
#             prefix_sum - goal = 0 (exists in prefix_sums, add prefix_sums[0] to count)
#             count = 1
#             Update prefix_sums: {0: 1, 1: 1, 2: 1}
#         Step 3: Current element 0
#             prefix_sum = 2
#             prefix_sum - goal = 0 (exists in prefix_sums, add prefix_sums[0] to count)
#             count = 2
#             Update prefix_sums: {0: 1, 1: 1, 2: 2}
#         Step 4: Current element 1
#             prefix_sum = 3
#             prefix_sum - goal = 1 (exists in prefix_sums, add prefix_sums[1] to count)
#             count = 3
#             Update prefix_sums: {0: 1, 1: 1, 2: 2, 3: 1}
#         Step 5: Current element 1
#             prefix_sum = 4
#             prefix_sum - goal = 2 (exists in prefix_sums, add prefix_sums[2] to count)
#             count = 5
#             Update prefix_sums: {0: 1, 1: 1, 2: 2, 3: 1, 4: 1}

# Final count is 5.

# Complexity Analysis
# Time Complexity

# The time complexity of this algorithm is O(n)

# , where n is the number of elements in the input array nums. This is because we iterate through the array once, and each operation inside the loop (like updating the prefix sum and hashmap) is done in constant time.
# Space Complexity

# The space complexity of this algorithm is O(n)
# , where n is the number of elements in the input array nums. This is because, in the worst case, we might store every prefix sum in the hashmap. If all prefix sums are unique, the hashmap will have n entries.

class Solution:
    def num_subarrays_with_sum(self, nums, goal):
        count = 0
        prefix_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_sums:
                count += prefix_sums[prefix_sum-goal]
            if prefix_sum in prefix_sums:
                prefix_sums[prefix_sum] += 1
            else:
                prefix_sums[prefix_sum] = 1

        return count


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 0, 1, 1]
    goal1 = 2
    print(sol.num_subarrays_with_sum(nums1, goal1))  # Expected output: 5

    nums2 = [1, 1, 1, 1, 0, 0]
    goal2 = 3
    print(sol.num_subarrays_with_sum(nums2, goal2))  # Expected output: 4

    nums3 = [0, 0, 0, 0, 1, 0, 1]
    goal3 = 1
    print(sol.num_subarrays_with_sum(nums3, goal3))  # Expected output: 12


# Time Complexity
# The time complexity of this algorithm is O(n), where n is the number of elements in the input array nums. This is because we iterate through the array once, and each operation inside the loop (like updating the prefix sum and hashmap) is done in constant time.

# Space Complexity
# The space complexity of this algorithm is O(n), where n is the number of elements in the input array nums. This is because, in the worst case, we might store every prefix sum in the hashmap. If all prefix sums are unique, the hashmap will have n entries.
