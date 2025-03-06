# Given an array of numbers sorted in ascending order and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target. If no such pair exists return [-1, -1].

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

# Since the given array is sorted, a brute-force solution could be to iterate through the array, taking one number at a time and searching for the second number through Binary Search. The time complexity of this algorithm will be . Can we do better than this?

# To solve this problem, we can use a two-pointer approach. This approach is efficient because it takes advantage of the sorted nature of the array. By starting with one pointer at the beginning and the other at the end, we can adjust their positions based on the sum of the elements they point to. This allows us to find the pair that adds up to the target without needing to check all possible pairs, which saves time.

# By moving the pointers inward, we can systematically find the pair in a single pass through the array. This ensures that the solution is both time-efficient and easy to implement.

# Let's walk through the example with input [1, 2, 3, 4, 6] and target 6.

# Initialize pointers: left = 0, right = 4
# First iteration:
# currentSum = 1 + 6 = 7 (greater than target)
# Decrement right to 3
# Second iteration:
# currentSum = 1 + 4 = 5 (less than target)
# Increment left to 1
# Third iteration:
# currentSum = 2 + 4 = 6 (equals target)
# Return indices [1, 3]

# TC: O(N)
# SC: O(1)

class Solution:
    def search(self, arr, target):
        left, right = 0, len(arr)-1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                return [left, right]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


def main1():
    sol = Solution()
    print(sol.search([1, 2, 3, 4, 6], 6))
    print(sol.search([2, 5, 9, 11], 11))


main1()


# An Alternate approach
# Instead of using a two-pointer or a binary search approach, we can utilize a HashTable to search for the required pair. We can iterate through the array one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ such that “X+Y == Target”. We will do two things here:

# Search for ‘Y’ (which is equivalent to “Target−X”) in the HashTable. If it is there, we have found the required pair. Otherwise, insert “X” in the HashTable, so that we can search it for the later numbers.

class Solution2:
    def search(self, arr, target):
        nums = {}
        for i, num in enumerate(arr):
            if target-num in nums:
                return [nums[target-num], i]
            else:
                nums[num] = i
        return [-1, -1]


def main():
    sol = Solution2()
    print(sol.search([1, 2, 3, 4, 6], 6))
    print(sol.search([2, 5, 9, 11], 11))


main()

# TC: O(N)
# SC: O(N)
# In summary, the algorithm has an average time complexity of O(n) and a space complexity of O(n). The time complexity can degrade to O(n^2) in the worst case due to potential hash collisions, but this is generally not the common case with a good hash function.
