# Given a binary matrix that has dimensions m*n , consisting of ones and zeros, determine the row that contains the highest number of ones and return two values: the zero-based index of this row and the actual count of ones it possesses.

# If there is a tie, i.e., multiple rows contain the same maximum number of ones, we must select the row with the lowest index.

class Solution:
    def findRowMaxOnes(self,mat):
        maxOnesIdx, maxOnesCount = 0, 0
        for i,row in enumerate(mat):
            onesCount = sum(row)
            if onesCount > maxOnesCount:
                maxOnesIdx, maxOnesCount = i, onesCount
        return [maxOnesIdx, maxOnesCount]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findRowMaxOnes([[1, 0], [1, 1], [0, 1]]))  # Output: [1, 2]   
    print(sol.findRowMaxOnes([[0, 1, 1], [0, 1, 1], [1, 1, 1]]))  # Output: [2, 3]
    print(sol.findRowMaxOnes([[1, 0, 1], [0, 0, 1], [1, 1, 0]]))  # Output: [0, 2]