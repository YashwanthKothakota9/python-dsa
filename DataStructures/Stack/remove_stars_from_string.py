# Given a string s, where * represents a star. We can remove a star along with its closest non-star character to its left in a single operation.

# The task is to perform as many such operations as possible until all stars have been removed and return the resultant string.

# Input: "abc*de*f"
# Expected Output: "abdf"
# Description: We remove c along with * to get "abde*f", then remove e along with * to get "abdf"

class Solution:
    def remove_stars(self,s):
        stack = []
        for char in s:
            if char == '*' and stack:
                stack.pop()
            elif char != '*':
                stack.append(char)
        return ''.join(stack)
    
def main():
    sol = Solution()
    print(sol.remove_stars("abc*de*f"))  # Output: "abdf"
    print(sol.remove_stars("a*b*c*d"))  # Output: "d"
    print(sol.remove_stars("abcd"))  # Output: "abcd"

if __name__ == '__main__':
    main()