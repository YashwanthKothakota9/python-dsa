# Given an input array of integers nums, find an integer array, let's call it differenceArray, of the same length as an input integer array.

# Each element of differenceArray, i.e., differenceArray[i], should be calculated as follows: take the sum of all elements to the left of index i in array nums (denoted as leftSum[i]), and subtract it from the sum of all elements to the right of index i in array nums (denoted as rightSum[i]), taking the absolute value of the result. Formally:

# differenceArray[i] = | leftSum[i] - rightSum[i] |

# If there are no elements to the left/right of i, the corresponding sum should be taken as 0.

# Example 1:

# Input: [2, 5, 1, 6]
# Expected Output: [12, 5, 1, 8]
# Explanation:
# For i=0: |(0) - (5+1+6)| = |0 - 12| = 12
# For i=1: |(2) - (1+6)| = |2 - 7| = 5
# For i=2: |(2+5) - (6)| = |7 - 6| = 1
# For i=3: |(2+5+1) - (0)| = |8 - 0| = 8

class Solution:
    def findDifferenceArray(self,nums):
        n = len(nums)
        leftSum = [0]*n
        rightSum = [0]*n
        diffArray = [0]*n

        leftSum[0] = nums[0]
        for i in range(1,n):
            leftSum[i] = leftSum[i-1] + nums[i]
        
        rightSum[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            rightSum[i] = rightSum[i+1] + nums[i]

        for i in range(n):
            diffArray[i] = abs(leftSum[i] - rightSum[i])
        
        return diffArray
    
if __name__ == "__main__":
    solution = Solution()
    example1 = [2, 5, 1, 6]
    example2 = [3, 1, 4, 2, 2]
    example3 = [1, 2, 3, 4, 5]
    
    # Output should be: [12, 5, 1, 8]
    print(solution.findDifferenceArray(example1))
    # Output should be: [9, 5, 0, 6, 10]
    print(solution.findDifferenceArray(example2))
    # Output should be: [14, 11, 6, 1, 10]
    print(solution.findDifferenceArray(example3))