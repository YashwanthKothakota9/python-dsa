# Given an m x n grid of characters board and a string word, return true if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:

# Input: word="ABCCED", board:

#   { 'A', 'B', 'C', 'E' },
#   { 'S', 'F', 'C', 'S' },
#   { 'A', 'D', 'E', 'E' }
# Output: true

# Explanation: The word exists in the board:
# -> { 'A', 'B', 'C', 'E' },
# -> { 'S', 'F', 'C', 'S' },
# -> { 'A', 'D', 'E', 'E' }

# Example 2:

# Input: word="SEE", board:

#   { 'A', 'B', 'C', 'E' },
#   { 'S', 'F', 'C', 'S' },
#   { 'A', 'D', 'E', 'E' }
# Output: true

# Explanation: The word exists in the board:
# -> { 'A', 'B', 'C', 'E' },
# -> { 'S', 'F', 'C', 'S' },
# -> { 'A', 'D', 'E', 'E' }


# The basic approach to solving the word search problem using backtracking is to start at the first character of the word and check all 4 adjacent cells in the grid to see if any of them match the next character of the word. If a match is found, mark the cell as visited and recursively check the next character of the word in the adjacent cells of the newly visited cell. If the entire word is found, return true. If no match is found, backtrack to the previous cell and try a different path. Repeat this process until the entire grid has been searched or the word is found.

# This function takes a 2D list board and a string word as input, and returns True if the word can be found in board and False otherwise. It uses a helper function dfs which takes 4 additional parameters: i and j are the current coordinates of the cell that is being visited, k is the index of the current character of the word being matched, and board and word are the inputs passed to the main function.

# The dfs function uses a helper variable tmp to store the current value of the cell before it is marked as visited. This is done so that we can backtrack later. It then uses recursion to check if the next character of the word exists in the 4 adjacent cells, and it will mark the cell as visited and move to next index of the word by incrementing k by 1. If the next character is found, the function returns true, if not it backtracks to the previous cell, and continues the search in different path. If the entire word is found, the function returns True, otherwise it returns False after searching the entire grid.

class Solution:
    def dfs(self, board, word, i, j, k):
        # check if current coordinates are out of grid or the current cell doesn't match the current character of the word
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False

        # check if we have reached the end of the word
        if k == len(word)-1:
            return True

        # mark the current cell as visited by replacing it with '/'
        tmp, board[i][j] = board[i][j], '/'

        # check all 4 adjacent cells recursively
        res = self.dfs(board, word, i+1, j, k+1) or \
            self.dfs(board, word, i-1, j, k+1) or \
            self.dfs(board, word, i, j+1, k+1) or \
            self.dfs(board, word, i, j-1, k+1)

        # backtrack by replacing the current cell with its original value
        board[i][j] = tmp
        return res

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                # start the search from every cell
                if self.dfs(board, word, i, j, 0):
                    return True
        return False


def main():
    sol = Solution()
    # Test Case 1
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(sol.exist(board, word))  # expected output: True

    # Test Case 2
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "SEE"
    print(sol.exist(board, word))  # expected output: True

    # Test Case 3
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCB"
    print(sol.exist(board, word))  # expected output: False

    # Test Case 4
    board = [['a', 'a']]
    word = "aaa"
    print(sol.exist(board, word))  # expected output: False

    # Test Case 5
    board = [['a']]
    word = "a"
    print(sol.exist(board, word))  # expected output: True

    # Test Case 6
    board = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['k', 'l', 'm', 'n', 'o'],
        ['p', 'q', 'r', 's', 't'],
        ['u', 'v', 'w', 'x', 'y'],
        ['z', 'a', 'b', 'c', 'd']
    ]
    word = "abcde"
    print(sol.exist(board, word))  # expected output: True

    # Test Case 7
    board = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['k', 'l', 'm', 'n', 'o'],
        ['p', 'q', 'r', 's', 't'],
        ['u', 'v', 'w', 'x', 'y'],
        ['z', 'a', 'b', 'c', 'd']
    ]
    word = "zabcd"
    print(sol.exist(board, word))  # expected output: True


main()


# Time Complexity
# The overall time complexity of the algorithm is O(M.N.4^L)

# (M.N): Number of cells in the board.
# (4^L): Each cell can lead to up to 4 recursive calls (one for each direction: up, down, left, right). For a word of length (L), there are up to (4^L) : possible paths to explore.
# Thus, for each cell, the DFS can potentially explore (4^L) : paths. Since the search starts from every cell, the overall complexity is O(M.N.4^L).


# Space Complexity
# The space complexity of the exist function is O(n), where n is the length of the word. This is because the function uses a DFS algorithm, and the maximum depth of the recursion tree is n. In other words, the maximum number of function calls that will be stored on the call stack at any point in time is n.
