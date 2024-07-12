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

class Solution:
    def removeDuplicates(self, s:str) -> str:
        count = {char: s.count(char) for char in set(s)}
        # print(count)
        result = []
        present = set()
        
        for char in s:
            # Only add character if it's not already in the result
            if char not in present:
                # Ensure the smallest lexicographical order
                while result and char < result[-1] and count[result[-1]] > 0:
                    present.remove(result.pop())
                result.append(char)
                present.add(char)
            count[char] -= 1
        return ''.join(result)
    
sol = Solution()
print(sol.removeDuplicates("bbaac"))    # Output: "bac"
print(sol.removeDuplicates("zabccde")) # Output: "zabcde"
print(sol.removeDuplicates("mnopmn"))   # Output: "mnop"


