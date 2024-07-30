# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.

# Examples

# Input: s = "abccba"
# Output: ""
# Explanation: First, we remove "cc" to get "abba". Then, we remove "bb" to get "aa". Finally, we remove "aa" to get an empty string.
# Input: s = "foobar"
# Output: "fbar"
# Explanation: We remove "oo" to get "fbar".


class Solution:
    def removeDuplicates(self, s:str) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("abccba")) # Output: ""
    print(solution.removeDuplicates("foobar")) # Output: "fbar"
    print(solution.removeDuplicates("abcd")) # Output: "abcd"
    

# The time complexity of this algorithm is O(N), where N is the length of s, because we perform one operation per character in s. The space complexity is also O(N), as in the worst case, every character in s is pushed onto the stack.