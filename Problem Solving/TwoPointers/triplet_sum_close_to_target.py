# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: The triplet [-1, 0, 3] has the sum '2' which is closest to the target.

# There are two triplets with distance '1' from the target: [-1, 0, 3] & [-1, 2, 3]. Between these two triplets, the correct answer will be [-1, 0, 3] as it has a sum '2' which is less than the sum of the other triplet which is '4'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'

# Tc: O(N^2) Sc: O(N)

import math

class Solution:
    def searchTriplet(self, arr, targetSum):
        arr.sort()
        smallest_diff = math.inf
        for i in range(len(arr)-2):
            left = i+1
            right = len(arr)-1
            
            while left < right:
                target_diff = targetSum - arr[i] - arr[left] - arr[right]
                if target_diff == 0:
                    return targetSum
                
                if abs(target_diff) < abs(smallest_diff) \
                    or ( abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                        smallest_diff = target_diff
                
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
        return targetSum - smallest_diff


def main():
  sol = Solution()
  print(sol.searchTriplet([-1, 0, 2, 3], 2))
  print(sol.searchTriplet([-3, -1, 1, 2], 1))
  print(sol.searchTriplet([1, 0, 1, 1], 100))
  print(sol.searchTriplet([0, 0, 1, 1, 2, 6], 5))


main()
                    