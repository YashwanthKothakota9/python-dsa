# Given a string, write a function that uses a stack to reverse the string. The function should return the reversed string.

# Examples
# Example 1:

# Input: "Hello, World!"
# Output: "!dlroW ,olleH"

# Define a class named Solution
class Solution:
    # Define a method called reverseString within the class
    def reverseString(self, s):
        # Convert the input string 's' into a list of characters and store it in the 'stack' variable
        stack = list(s)
        # Initialize an empty string to store the reversed string
        reversed_str = ''
        
        # Use a loop to pop characters from the 'stack' and append them to 'reversed_str'
        # This effectively reverses the order of characters in the string
        while stack:
            reversed_str += stack.pop()
        
        # Return the reversed string
        return reversed_str

# Create an instance of the Solution class
rs = Solution()

# Test the reverseString method with different input strings and print the results
print(rs.reverseString("Hello, World!"))  # Output: "!dlroW ,olleH"
print(rs.reverseString("OpenAI"))  # Output: "IAnepO"
print(rs.reverseString("Stacks are fun!"))  # Output: "!nuf era skcatS"


# Time Complexity:O(n) , where n is the length of the input string. This is because we iterate through the string once to push all characters into the stack and then another time to pop all characters out of the stack.

# Space Complexity:O(n) , where n is the length of the input string. This is because we use a stack to hold all characters of the string.