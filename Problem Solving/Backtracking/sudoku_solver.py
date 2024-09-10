# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:
# Input:

#             {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
#             {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
#             {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
#             {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
#             {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
#             {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
#             {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
#             {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
#             {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
# Output:

#             {'5'', '3'', '4'', '6'', '7'', '8'', '9'', '1'', '2''},
#             {'6'', '7'', '2'', '1'', '9'', '5'', '3'', '4'', '8''},
#             {'1'', '9'', '8'', '3'', '4'', '2'', '5'', '6'', '7''},
#             {'8'', '5'', '9'', '7'', '6'', '1'', '4'', '2'', '3''},
#             {'4'', '2'', '6'', '8'', '5'', '3'', '7'', '9'', '1''},
#             {'7'', '1'', '3'', '9'', '2'', '4'', '8'', '5'', '6''},
#             {'9'', '6'', '1'', '5'', '3'', '7'', '2'', '8'', '4''},
#             {'2'', '8'', '7'', '4'', '1'', '9'', '6'', '3'', '5''},
#             {'3'', '4'', '5'', '2'', '8'', '6'', '1'', '7'', '9''}

# Explanation: The given output is the only valid Sudoku solution


# To solve the Sudoku puzzle, we use a backtracking approach. The key idea is to fill each empty cell with numbers from 1 to 9 and validate if the number can fit into the cell without violating the Sudoku rules. The rules are that each number must be unique in its row, column, and 3x3 sub-box. If a number fits, we proceed to the next empty cell recursively. If we encounter a cell where no number fits, we backtrack by resetting the previous cell and trying the next possible number. This process continues until the entire board is filled correctly.

# This approach works because it explores all possible combinations and backtracks whenever it encounters a wrong combination, ensuring that we eventually find a solution if one exists. The efficiency is maintained by the early pruning of invalid paths, thus reducing unnecessary computations.

# Step-by-Step Algorithm
# Initialization:

# Define a helper function isValid to check if a number can be placed in a given cell without violating the Sudoku rules.
# Define the main function solveSudoku that takes the board as input and calls the recursive solve function to fill the board.
# Validation Helper Function:

# For a given cell (row, col) and number num, iterate over each cell in the same row, column, and 3x3 sub-box.
# Check if the number num already exists in the same row, column, or sub-box.
# Return True if num does not exist in any of these, otherwise return False.
# Recursive Solver Function:

# Iterate over each cell in the board.
# If an empty cell (denoted by .) is found, try placing each number from 1 to 9 in the cell.
# Use the isValid function to check if the number can be placed in the cell.
# If valid, place the number in the cell and recursively call the solve function.
# If the recursive call returns True, the board is solved, so return True.
# If placing the number does not lead to a solution, backtrack by resetting the cell to . and try the next number.
# If no number from 1 to 9 can be placed in the cell, return False to indicate a dead end.
# Completion:

# If the entire board is filled without conflicts, the solve function returns True.
# The solveSudoku function then returns the solved board.


class Solution:
    # Helper function to check if a given number is valid in the current cell
    def isValid(self, board, row, col, num):
        # Check if we already have the same number in the same row, col or box
        for x in range(9):
            if board[row][x] == num:
                return False  # Check if the same number is in the same row
            if board[x][col] == num:
                return False  # Check if the same number is in the same col
            if board[(row//3)*3 + x//3][(col//3)*3 + x % 3] == num:
                return False  # Check if the same number is in the same 3x3 box
        return True

    # Solves the Sudoku and returns the solved board
    def solveSudoku(self, board):
        self.solve(board)
        return board

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # If we find an empty cell
                    for num in range(1, 10):  # Try every number from 1-9
                        # Check if the number is valid in the current cell
                        if self.isValid(board, row, col, str(num)):
                            # If it is valid, fill the cell with the number
                            board[row][col] = str(num)
                            # Recursively call the function to solve the rest of the board
                            if self.solve(board):
                                return True
                            else:  # If the current number doesn't lead to a solution, backtrack by emptying the cell
                                board[row][col] = '.'
                    return False  # If we have tried every number and none of them lead to a solution, return false
        return True  # If the board is completely filled, return true


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

solvedBoard1 = sol.solveSudoku(board1)
for row in solvedBoard1:
    print(" ".join(row))

print("-"*50)

board2 = [
    ['8', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '3', '6', '.', '.', '.', '.', '.'],
    ['.', '7', '.', '.', '9', '.', '2', '.', '.'],
    ['.', '5', '.', '.', '.', '7', '.', '.', '.'],
    ['.', '.', '.', '.', '4', '5', '7', '.', '.'],
    ['.', '.', '.', '1', '.', '.', '.', '3', '.'],
    ['.', '.', '1', '.', '.', '.', '.', '6', '8'],
    ['.', '.', '8', '5', '.', '.', '.', '1', '.'],
    ['.', '9', '.', '.', '.', '.', '4', '.', '.']
]

solvedBoard2 = sol.solveSudoku(board2)
for row in solvedBoard2:
    print(" ".join(row))


# Time Complexity
# since the board size is fixed, the time complexity is O(1), as there is no variable input.

# Though let's discuss the number of operations needed:(9!)^9

# Let's consider one row where we have 9 cells to fill. There are not more than 9 possibilities for the first number to put, not more than 9×8 for the second one, not more than 9×8×7 for the third one, and so on. In total, that results in not more than (9!) possibilities for just one row; this means not more than (9!)^9 operations in total.

# If we compare the brutefore and backtracking algorithms:

#  9^81= 1966270504755529136180759085269121162831034509442147669273154155379663911968099 for the brute force,

# and (9!)^9=109110688415571316480344899355894085582848000000000 for the standard backtracking, i.e. the number of operations is reduced in  10^27 times!

# Space Complexity
# The board size is fixed, and the space is used to store the board containing 81 cells, hence the time complexity is O(1).
