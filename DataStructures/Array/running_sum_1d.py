class Solution:
    def runningSum(self,nums):
        result = [0]*len(nums)
        result[0] = nums[0]
        for i in range(1,len(nums)):
            result[i] = result[i-1] + nums[i]
        return result
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.runningSum([2, 3, 5, 1, 6]))  # Output: [2, 5, 10, 11, 17]
    print(sol.runningSum([1, 1, 1, 1, 1]))  # Output: [1, 2, 3, 4, 5]
    print(sol.runningSum([-1, 2, -3, 4, -5]))  # Output: [-1, 1, -2, 2, -3]
