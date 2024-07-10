# Given a string of English lowercase and uppercase letters, make the string "good" by removing two adjacent characters that are the same but in different cases.

# Continue to do this until there are no more adjacent characters of the same letter but in different cases. An empty string is also considered "good".

# Input: "AaBbCcDdEeff"
# Output: "ff"
# Explanation: In the first step, "AaBbCcDdEeff" becomes "BbcCDdEeff" because 'A' and 'a' are the same letter, but one is uppercase and the other is lowercase. Then we remove "Bb", and then "cC", "dD", and "Ee". In the end we are left with "ff" which we can't remove - although both characters are the same but with the same case.

class Solution:
    def make_string_good(self, s):
        stack = []
        for c in s:
            if stack and stack[-1].swapcase() == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

def main():
    sol = Solution()
    print(sol.make_string_good("AaBbCcDdEeff"))  # Output: "ff"
    print(sol.make_string_good("abBA"))  # Output: ""
    print(sol.make_string_good("s"))  # Output: "s"

if __name__ == '__main__':
    main()