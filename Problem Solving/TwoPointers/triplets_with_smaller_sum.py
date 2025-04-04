# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
# [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

# Following a similar approach, first, we can sort the array and then iterate through it, taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X+Y+Z<target . At this stage, our problem translates into finding a pair whose sum is less than “target-X” (as from the above equation Y+z<target-X ). We can use a similar approach as discussed in "Triplet Sum to Zero".

# Tc: O(N^2) Sc: O(N)

class Solution:
    def searchTriplets(self, arr, target):
        if len(arr) < 3:
            return 0
        
        arr.sort()
        count = 0
        for i in range(len(arr)-2):
            count += self.searchPair(arr, target-arr[i], i)
        return count

    def searchPair(self, arr, targetSum, first):
        count = 0
        left, right = first+1, len(arr)-1
        while left < right:
            if arr[left] + arr[right] < targetSum:
                # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between left and right to get a sum less than the target sum
                count += right - left
                left += 1
            else:
                right -= 1
        return count


def main():
  sol = Solution()
  print(sol.searchTriplets([-1, 0, 2, 3], 3))
  print(sol.searchTriplets([-1, 4, 2, 1, 3], 5))


main()
