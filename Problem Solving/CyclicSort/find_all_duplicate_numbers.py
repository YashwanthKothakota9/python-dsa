# We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice, find all these duplicate numbers using constant space.

# Example 1:

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:

# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]

class Solution:
    def findNumbers(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        
        duplicateNumbers = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                duplicateNumbers.append(nums[i])
        
        return duplicateNumbers

def main():
  sol = Solution()
  print(sol.findNumbers([3, 4, 4, 5, 5]))
  print(sol.findNumbers([5, 4, 7, 2, 3, 5, 3]))

main()