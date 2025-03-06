# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:

# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:

# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.


# Algorithm Walkthrough
# Input: str1 = "xp#", str2 = "xyz##"

# Initial pointers: index1 = 2, index2 = 4
# Process str1 (xp#):
# index1 = 2 (points to #): increment backspaceCount = 1, move index1 to 1
# index1 = 1 (points to p): decrement backspaceCount = 0, move index1 to 0
# index1 = 0 (points to x): valid character found
# Process str2 (xyz##):
# index2 = 4 (points to #): increment backspaceCount = 1, move index2 to 3
# index2 = 3 (points to #): increment backspaceCount = 2, move index2 to 2
# index2 = 2 (points to z): decrement backspaceCount = 1, move index2 to 1
# index2 = 1 (points to y): decrement backspaceCount = 0, move index2 to 0
# index2 = 0 (points to x): valid character found
# Compare characters:
# Both characters are x (equal), move index1 to -1 and index2 to -1
# End of strings: Both pointers are less than zero, strings are equal.

# TC: O(N+M)
# SC: O(1)


class Solution:
    def compare(self, str1, str2):
        index1 = len(str1)-1
        index2 = len(str2)-1
        while index1 >= 0 or index2 >= 0:
            i1 = self.get_next_valid_char_index(str1, index1)
            i2 = self.get_next_valid_char_index(str2, index2)
            if i1 < 0 and i2 < 0:  # reached the end of both the strings
                return True
            if i1 < 0 or i2 < 0:  # reached the end of one of the strings
                return False
            if str1[i1] != str2[i2]:  # check if the characters are equal
                return False
            index1 = i1-1
            index2 = i2-1
        return True

    def get_next_valid_char_index(self, str, index):
        backspace_count = 0
        while index >= 0:
            if str[index] == '#':  # found a backspace character
                backspace_count += 1
            elif backspace_count > 0:  # a non-backspace character
                backspace_count -= 1
            else:
                break
            index -= 1  # skip a backspace or a valid character
        return index


def main():
    sol = Solution()
    print(sol.compare("xy#z", "xzz#"))
    print(sol.compare("xy#z", "xyz#"))
    print(sol.compare("xp#", "xyz##"))
    print(sol.compare("xywrrmp", "xywrrmu#p"))


main()
