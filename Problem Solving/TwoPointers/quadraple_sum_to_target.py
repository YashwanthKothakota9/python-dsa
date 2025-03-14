# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

# Example 1:
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# Example 2:
# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# This problem follows the Two Pointers pattern and shares similarities with "Triplet Sum to Zero".

# We can follow a similar approach to iterate through the array, taking one number at a time. At every step during the iteration, we will search for the quadruplets similar to Triplet Sum to Zero whose sum is equal to the given target.

# TC: O(N^3) Sc: O(N)

class Solution:
    def searchQuadraplets(self, arr, target):
        arr.sort()
        quadraplets = []
        for i in range(len(arr)-3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1, len(arr)-2):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                self.searchPairs(arr, target, i, j, quadraplets)
        return quadraplets
    
    def searchPairs(self, arr, targetSum, first, second, quadraplets):
        left = second + 1
        right = len(arr)-1
        while left < right:
            quadSum = arr[first] + arr[second] + arr[left] + arr[right]
            if quadSum == targetSum:
                quadraplets.append([arr[first], arr[second], arr[left], arr[right]])
                left += 1
                right -= 1
                while (left < right and arr[left] == arr[left - 1]):
                    left += 1  # skip same element to avoid duplicate quadruplets
                while (left < right and arr[right] == arr[right + 1]):
                    right -= 1  # skip same element to avoid duplicate quadruplets
            elif quadSum < targetSum:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum


def main():
  sol = Solution()
  print(sol.searchQuadraplets([4, 1, 2, -1, 1, -3], 1))
  print(sol.searchQuadraplets([2, 0, -1, 1, -2, 2], 2))


main()