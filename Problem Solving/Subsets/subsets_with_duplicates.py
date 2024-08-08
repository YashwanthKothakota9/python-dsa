# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# Example 1:

# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]
# Example 2:

# Input: [1, 5, 3, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 

class Solution:
    def findSubsets(self, nums):
        # sort the numbers to handle duplicates
        list.sort(nums)
        subsets = []
        subsets.append([])
        endIndex = 0
        for i in range(len(nums)):
            startIndex = 0
            # if current and the previous elements are same, create new subsets only from the subsets added in the previous step
            if i > 0 and nums[i] == nums[i-1]:
                startIndex = endIndex + 1
            endIndex = len(subsets)-1
            for j in range(startIndex, endIndex+1):
                # create a new subset from the existing subset and add the current element to it
                set1 = list(subsets[j])
                set1.append(nums[i])
                subsets.append(set1)
        return subsets

def main():
  sol = Solution()
  print("Here is the list of subsets: " + str(sol.findSubsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(sol.findSubsets([1, 5, 3, 3])))


main()


# Time Complexity
# Since, in each step, the number of subsets doubles (if not duplicate) as we add each element to all the existing subsets, therefore, we will have a total of O(2^N) subsets, where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N*2^N).

# Space Complexity
# All the additional space used by our algorithm is for the output list. Since, at most, we will have a total of O(2^N) subsets, and each subset can take up to O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N).