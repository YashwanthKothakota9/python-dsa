# Given a string s containing (, ), [, ], {, and } characters. Determine if a given string of parentheses is balanced.

# A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis in the correct order.

# Example 1:

# Input: String s = "{[()]}";
# Expected Output: true
# Explanation: The parentheses in this string are perfectly balanced. Every opening parenthesis '{', '[', '(' has a corresponding closing parenthesis '}', ']', ')' in the correct order.

# Example 2:

# Input: string s = "{[}]";
# Expected Output: false
# Explanation: The brackets are not balanced in this string. Although it contains the same number of opening and closing brackets for each type, they are not correctly ordered. The ']' closes '[' before '{' can be closed by '}', and similarly, '}' closes '{' before '[' can be closed by ']'.

class Solution:
    def isValid(self,s:str)->bool:
        stack = []
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c==')' and top!='(':
                    return False
                if c=='}' and top!='{':
                    return False
                if c==']' and top!='[':
                    return False
        # If the stack is empty, all opening parentheses had a corresponding closing match
        return not stack
    
def main():
    sol = Solution()
    test1 = "{[()]}"; # Should be valid
    test2 = "{[}]";   # Should be invalid
    test3 = "(]";     # Should be invalid

    print("Test 1:", sol.isValid(test1))
    print("Test 2:", sol.isValid(test2))
    print("Test 3:", sol.isValid(test3))

if __name__ == '__main__':
    main()