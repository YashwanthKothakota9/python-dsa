# Give a string s, convert it into a valid string. A string is considered valid if it does not have any two adjacent duplicate characters.

# To make a string valid, we will perform a duplicate removal process. A duplicate removal consists of choosing two adjacent and equal letters and removing them. We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.

# Input: "abbaca"
# Expected Output: "ca"
# Description: We remove 'b' from "abbaca" to get "aaca", then remove 'a' from "aaca" to get "ca"

# Tc: O(n) Sc: O(n)
class Solution:
    def remove_adjacent_duplicates(self, str_in):
        stack = []
        for char in str_in:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

def main():
    sol = Solution()
    print(sol.remove_adjacent_duplicates("abbaca"))  # Output: "ca"
    print(sol.remove_adjacent_duplicates("azxxzy"))  # Output: "ay"
    print(sol.remove_adjacent_duplicates("abbay"))    # Output: ""

if __name__ == '__main__':
    main()