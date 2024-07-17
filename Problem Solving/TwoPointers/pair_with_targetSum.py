# Given an array of numbers sorted in ascending order and a target sum, find a pair in the array whose sum is equal to the given target. If no such pair exists return [-1, -1].

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

# To solve this problem, we can use a two-pointer approach. This approach is efficient because it takes advantage of the sorted nature of the array. By starting with one pointer at the beginning and the other at the end, we can adjust their positions based on the sum of the elements they point to. This allows us to find the pair that adds up to the target without needing to check all possible pairs, which saves time.

# By moving the pointers inward, we can systematically find the pair in a single pass through the array. This ensures that the solution is both time-efficient and easy to implement.

# Tc: O(n) Sc: O(1)

class Solution:
    def pair_with_targetSum(self, arr, targetSum):
        left, right = 0, len(arr)-1
        
        while left < right:
            currSum = arr[left] + arr[right]
            if currSum == targetSum:
                return [left, right]
            if targetSum > currSum:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]

def main():
    sol = Solution()
    print(sol.pair_with_targetSum([1,2,3,4,6],6))
    print(sol.pair_with_targetSum([2,5,9,11], 11))

main()

# ----------------------------------------------

#  Using HashMap
def pair_with_targetSum(arr, targetSum):
    nums = {}
    for i, num in enumerate(arr):
        if targetSum - num in nums:
            return [nums[targetSum-num], i]
        else:
            nums[num] = i
    return [-1, -1]

# In summary, the algorithm has an average time complexity of (O(n)) and a space complexity of (O(n)). The time complexity can degrade to (O(n^2)) in the worst case due to potential hash collisions, but this is generally not the common case with a good hash function.