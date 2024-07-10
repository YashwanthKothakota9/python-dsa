class Solution:
    def diagonalSum(self,mat):
        n = len(mat)
        totalSum = 0

        for i in range(n):
            totalSum += mat[i][i] + mat[i][n-i-1]
            
        # If n is odd, subtract the central element
        if n%2 != 0:
            totalSum -= mat[n//2][n//2]
        return totalSum
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))  # Output: 25
    print(sol.diagonalSum([[1,0],[0,1]]))  # Output: 2
    print(sol.diagonalSum([[5]]))  # Output: 5