# Given a 2D matrix of size m x n, return the 1D array containing all elements of matrix in spiral order.

# Examples
# Example 1:

# Input: matrix =
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
#  [13, 14, 15, 16]]
# Expected Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

# Solution
# To solve this problem, we employ a systematic approach to traverse the matrix in layers, starting from the outermost layer and gradually moving towards the inner layers. We maintain four pointers to mark the boundaries of the current layer: top, bottom, left, and right. Initially, these pointers are set to the boundaries of the matrix. In each iteration, we traverse the current layer in a spiral order: from left to right, top to bottom, right to left, and bottom to top, adjusting the boundary pointers accordingly after each direction of traversal. This approach ensures that we visit each element exactly once, maintaining the spiral order.

# This method is effective because it clearly defines the traversal order and boundaries, preventing overlaps or missed elements. By systematically shrinking the traversal area and moving inward, we ensure complete coverage of the matrix in a spiral pattern. This logical progression mirrors the spiral traversal requirement, making it a natural fit for solving the problem

# Time Complexity
# o(m*n), where m * n is the total number of elements in the matrix. Each element is visited exactly once, making the time complexity linear in terms of the number of elements in the matrix.
# Space Complexity
# , disregarding the output array. The algorithm uses a constant amount of space for the pointers (top, bottom, left, right) and the result list's space is not considered part of the algorithm's space complexity as it is required for the output.
# If we consider the output space, then the space complexity is O(m*n), where m * n is the total number of elements in the matrix.


class Solution:
    def spiralOrder(self, matrix):
        result = []
        if not matrix or not matrix[0]:
            return result

        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1-1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1-1):
                    result.append(matrix[i][left])
                left += 1
        return result


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    matrix1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(sol.spiralOrder(matrix1))

    # Example 2
    matrix2 = [[1, 2], [3, 4], [5, 6]]
    print(sol.spiralOrder(matrix2))

    # Example 3 (Revised)
    matrix3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(sol.spiralOrder(matrix3))
