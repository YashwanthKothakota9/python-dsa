# Determine if a 9x9 Sudoku board is valid. A valid Sudoku board will hold the following conditions:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# The 9 3x3 sub-boxes of the grid must also contain the digits 1-9 without repetition.
# Note:

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# You need to validate only filled cells.
# Example 1:
# Input:
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Expected Output: true
# Justification: This Sudoku board is valid as it adheres to the rules of no repetition in each row, each column, and each 3x3 sub-box.
# Example 2:
# Input:
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Expected Output: false
# Justification: The first and fourth rows both contain the number '8', violating the Sudoku rules

# Solution
# Initialization:
# Create three hash sets for rows, columns, and boxes to keep track of the seen numbers.
# Iteration:
# Iterate through each cell in the 9x9 board.
# If the cell is not empty:
# Formulate keys for the row, column, and box that include the current number and its position.
# Check the corresponding sets for these keys.
# If any key already exists in the sets, return false.
# Otherwise, add the keys to the respective sets.
# Final Check:
# If the iteration completes without finding any repetition, return true.
# This approach works because it checks all the necessary conditions for a valid Sudoku by keeping track of the numbers in each row, column, and box using hash sets. The use of hash sets allows for efficient lookups to ensure no numbers are repeated in any row, column, or box.

# Complexity Analysis
# Time Complexity: O(1) or O(81), as we only iterate through the 9x9 board once.
# Space Complexity: O(1) or O(81), as the maximum size of our sets is 81.


class Solution:
    def isValidSudoku(self, board):
        rows = set()
        cols = set()
        boxes = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row_key = f"row{i}({num})"
                    col_key = f"col{j} ({num})"
                    box_key = f"box{i//3*3 + j//3}({num})"
                    print(f"{row_key}:{col_key}:{box_key}")
                    if (row_key in rows or col_key in cols or box_key in boxes):
                        return False
                    rows.add(row_key)
                    cols.add(col_key)
                    boxes.add(box_key)
        return True


sol = Solution()
board1 = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]
print(sol.isValidSudoku(board1))  # Output: True
