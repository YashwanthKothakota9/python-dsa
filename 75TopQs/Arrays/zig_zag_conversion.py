# Given a string s and a numRows integer representing the number of rows, write the string in a zigzag pattern on the given number of rows and then read it line by line, and return the resultant string.

# The zigzag pattern means writing characters in a diagonal down-and -up fashion. For example, given the string "HELLOPROGRAMMING" and 4 rows, the pattern would look like:

# H     R     M
# E   P O   M I
# L O   G A   N
# L     R     G
# Reading it line by line gives us "HRMEPOMILOGANLRG".

# Example 2:
# Input: s = "PROBLEMCHALLENGE", numRows = 5
# Expected Output: "PHRCAEOMLGBELNLE"
# Explanation: The zigzag pattern is :
# P       H
# R     C A     E
# O   M   L   G
# B E     L N
# L       E
# Reading line by line gives "LCCETEHLDELOEGAEEN".
# Example 3:
# Input: s = "ABCDE", numRows = 2
# Expected Output: "ACEBD"
# Explanation: The zigzag pattern is :
# A C E
# B D
# Reading line by line gives "ACEBD".
# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters(lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

# Algorithm Walkthrough
# Using the input s = "HELLOPROGRAMMING", numRows = 4:

# Edge Case Handling:

# numRows is 4, not 1, so we proceed.
# Initialize Rows:

# rows = ["", "", "", ""]
# Set Direction:

# currentRow = 0
# goingDown = False
# Place Characters:

# Iterate through the string "HELLOPROGRAMMING":

# 'H':

# rows[0] = "H"
# currentRow = 1
# goingDown = True
# 'E':

# rows[1] = "E"
# currentRow = 2
# goingDown = True
# 'L':

# rows[2] = "L"
# currentRow = 3
# goingDown = True
# 'L':

# rows[3] = "L"
# currentRow = 2
# goingDown = False
# 'O':

# rows[2] = "LO"
# currentRow = 1
# goingDown = False
# 'P':

# rows[1] = "EP"
# currentRow = 0
# goingDown = False
# 'R':

# rows[0] = "HR"
# currentRow = 1
# goingDown = True
# 'O':

# rows[1] = "EPO"
# currentRow = 2
# goingDown = True
# 'G':

# rows[2] = "LOG"
# currentRow = 3
# goingDown = True
# 'R':

# rows[3] = "LR"
# currentRow = 2
# goingDown = False
# 'A':

# rows[2] = "LOGA"
# currentRow = 1
# goingDown = False
# 'M':

# rows[1] = "EPOM"
# currentRow = 0
# goingDown = False
# 'M':

# rows[0] = "HRM"
# currentRow = 1
# goingDown = True
# 'I':

# rows[1] = "EPOMI"
# currentRow = 2
# goingDown = True
# 'N':

# rows[2] = "LOGAN"
# currentRow = 3
# goingDown = True
# 'G':

# rows[3] = "LRG"
# currentRow = 2
# goingDown = False
# Concatenate Rows:

# Join all rows to form the final zigzag string:
# result = "HRM" + "EPOMI" + "LOGAN" + "LRG"
# result = "HRMEPOMILOGANLRG"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # Create an array to hold rows
        rows = ['']*numRows
        currentRow = 0
        goingDown = False
        # Iterate through each character in the string
        for c in s:
            rows[currentRow] += c
            if currentRow == 0 or currentRow == numRows-1:
                goingDown = not goingDown
            currentRow += 1 if goingDown else -1
        return ''.join(rows)

    @staticmethod
    def main():
        solution = Solution()
        print(solution.convert("HELLOPROGRAMMING", 4))  # HRMEPOMILOGANLRG
        print(solution.convert("PROBLEMCHALLENGE", 5))  # PHRCAMLOEBLNGLEN
        print(solution.convert("ABCDE", 2))  # ACEBD


Solution.main()


# Complexity Analysis
# Time Complexity
# The time complexity of the algorithm is O(n), where n is the length of the input string. This is because we are iterating through each character in the string exactly once.

# Space Complexity
# The space complexity of the algorithm is O(n) as well. This is due to the array of strings used to hold the rows. Each character is stored exactly once in one of the rows, resulting in a total space requirement proportional to the length of the input string.
