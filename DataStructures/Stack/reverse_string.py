# Given a string, write a function that uses a stack to reverse the string. The function should return the reversed string.


class Solution:
    def reverseString(self,s):
        stack = list(s)
        reversed_str = ''
        while stack:
            reversed_str += stack.pop()
        return reversed_str

def main():
    rs = Solution()

    # Test the reverseString method with different input strings and print the results
    print(rs.reverseString("Hello, World!"))  # Output: "!dlroW ,olleH"
    print(rs.reverseString("OpenAI"))  # Output: "IAnepO"
    print(rs.reverseString("Stacks are fun!"))  # Output: "!nuf era skcatS"

if __name__ == '__main__':
    main()