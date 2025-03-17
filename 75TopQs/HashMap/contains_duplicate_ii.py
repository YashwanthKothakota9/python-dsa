# Given an array of integers nums and an integer k, return true if there are any two different indices i and j in the array where nums[i] == nums[j] and abs(i - j) <= k. Otherwise, return false.

# Examples
# Example 1:

# Input: nums = [10, 20, 10, 30], k = 1
# Output: false
# Explanation: The number 10 appears at positions 0 and 2. The difference between these positions is 2, which is not less than k.
# Example 2:

# Input: nums = [5, 15, 25, 5, 35], k = 3
# Output: true
# Explanation: The number 5 appears at positions 0 and 3. The difference between these positions is 3, which is equal to k.
# Example 3:

# Input: nums = [7, 8, 9, 7, 10, 11], k = 4
# Output: true
# Explanation: The number 7 appears at positions 0 and 3. The difference between these positions is 3, which is less than to k.

# To solve this problem, we'll use a hashmap to keep track of the last seen position of each number as we iterate through the array. This approach is efficient because it allows us to check in constant time whether a number has appeared before and whether the difference between the current position and the last seen position is less than or equal to k. By using a hashmap, we ensure that we only traverse the array once, making our solution fast.

# This approach is effective because it minimizes the number of operations required to find the solution, ensuring that we can handle large arrays efficiently.

# Complexity Analysis
# Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once, and each operation (insert and lookup in the hashmap) takes O(1) time.
# Space Complexity: O(n), where n is the number of elements in the array. In the worst case, all elements are stored in the hashmap.


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap and i-hashmap[num] <= k:
                return True
            hashmap[num] = i

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([10, 20, 10, 30], 1))  # false
    print(solution.containsNearbyDuplicate([5, 15, 25, 5, 35], 3))  # true
    print(solution.containsNearbyDuplicate([7, 8, 9, 7, 10, 11], 4))  # true
