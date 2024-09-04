# Given a string s, remove all duplicate letters from the input string while maintaining the original order of the letters.

# Additionally, the returned string should be the smallest in lexicographical order among all possible results.

# Examples:

# Input: "bbaac"
# Expected Output: "bac"
# Justification: Removing the extra 'b' and one 'a' from the original string gives 'bac', which is the smallest lexicographical string without duplicate letters.
# Input: "zabccde"
# Expected Output: "zabcde"
# Justification: Removing one of the 'c's forms 'zabcde', the smallest string in lexicographical order without duplicates.
# Input: "mnopmn"
# Expected Output: "mnop"
# Justification: Removing the second 'm' and 'n' gives 'mnop', which is the smallest possible string without duplicate characters.


# To solve the given problem, begin by iterating through the string, and calculate the frequency count for each character. We will use the stack to maintain the order of characters and the set to track the uniqueness of characters.

# Next, start traversing the string, and for every character encountered, check if it's already in the 'present' set. If it's not, compare it with the top element of the 'result' stack. If the stack is not empty, and the current character is lexicographically smaller than the stack's top, and the top character of the stack appears again in the string (indicated by a non-zero frequency count), repeatedly pop the stack and remove those elements from the 'present' set. Then, add the current character to the stack and the 'present' set.

# This process, facilitated by the stack and set, ensures that the stack is built with unique characters in the smallest lexicographical order. After processing the entire string, pop elements from the stack to construct the final string, thereby obtaining the smallest lexicographical sequence without duplicate characters.

# Frequency Count (count):

# Initialize a count dictionary (or hash map in some languages) to store the frequency of each character in the string s.
# Character Presence Tracking (present):

# Use a set present to keep track of the characters that have been added to the resultant string. This set prevents duplicate characters in the result.
# Building the Result (result):

# Create a stack result to construct the final string.
# For each character c in the string s:
# If c is not in present, proceed to compare it with the top character of result.
# While result is not empty, and c is lexicographically smaller than the top character of result, and the frequency of the top character of result is more than 0 (indicating it appears again in the string), pop the top character from result and remove it from present.
# Push c onto result and add it to present.
# Decrement the frequency of c in count.
# Result Construction:

# The stack result now contains the characters of the final string in reverse order. Pop elements from result to construct the output string in the correct order, from left to right.
# This approach works because it ensures that the smallest character is placed first, respecting the original order and removing duplicates. The frequency count ensures that characters are not wrongly discarded.

class Solution:
    def removeDuplicateLetters(self, s:str) -> str:
        # Count the frequency of each character
        count = {char:s.count(char) for char in set(s)}
        print(f"Set(s): {set(s)}")
        print(f"Count: {count}")
        result = [] # Stack for the result string
        present = set() # Set to track if a character is in the result
        
        for char in s:
            # Only add character if it's not already in the result
            if char not in present:
                # Ensure the smallest lexicographical order
                while result and char < result[-1] and count[result[-1]] > 0:
                    present.remove(result.pop())
                result.append(char)
                present.add(char)
            count[char] -= 1 # Decrease the frequency
        
        return ''.join(result)

sol = Solution()
print(sol.removeDuplicateLetters("bbaac"))    # Output: "bac"
print(sol.removeDuplicateLetters("zabccde")) # Output: "zabcde"
print(sol.removeDuplicateLetters("mnopmn"))   # Output: "mnop"


# Time Complexity: O(N) where N is the length of the string. Each character is visited once.
# Space Complexity: O(1) as the extra space used does not depend on the input size. The character count and the stack size are bounded by the character set size (constant).