# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# Explanation: There are four unique triplets whose sum is equal to zero. smallest sum.'
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

# Approach:
# This problem follows the Two Pointers pattern and shares similarities with Pair with Target Sum. A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets with a target sum of zero.

# To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that . At this stage, our problem translates into finding a pair whose sum is equal to “-X” (as from the above equation ).

# Another difference from Pair with Target Sum is that we need to find all the unique triplets. To handle this, we have to skip any duplicate number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and are easier to skip.


# Tc: O(N^2) Sc: O(1)

class Solution:
    def searchTriplets(self, arr):
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            self.searchPair(arr, -arr[i], i+1, triplets)
        return triplets
    
    def searchPair(self, arr, targetSum, left, triplets):
        right = len(arr)-1
        while left < right:
            currSum = arr[left] + arr[right]
            # found the triplet
            if currSum == targetSum:
                triplets.append([-targetSum, arr[left], arr[right]])
                left += 1
                right -= 1
                
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif targetSum > currSum:
                left += 1 # we need a pair with a bigger sum
            else:
                right -= 1 # we need a pair with a smaller sum


def main():
  sol = Solution()
  print(sol.searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
  print(sol.searchTriplets([-5, 2, -1, -2, 3]))


main()