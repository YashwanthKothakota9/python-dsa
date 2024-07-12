class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.searchMatrix(matrix1, 5))  # true

    # Example 2
    matrix2 = [[10,11,12,13],[11,12,13,17],[14,19,22,24],[22,23,24,25]]
    print(solution.searchMatrix(matrix2, 19))  # true

    # Example 3
    matrix3 = [[1,3,5],[7,9,11],[13,15,17]]
    print(solution.searchMatrix(matrix3, 6))  # false