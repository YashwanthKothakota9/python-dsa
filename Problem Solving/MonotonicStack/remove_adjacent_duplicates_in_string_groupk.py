# You are given a string s and an integer k. Your task is to remove groups of identical, consecutive characters from the string such that each group has exactly k characters. The removal of groups should continue until it's no longer possible to make any more removals. The result should be the final version of the string after all possible removals have been made.

# Examples

# Input: s = "abbbaaca", k = 3
# Output: "ca"
# Explanation: First, we remove "bbb" to get "aaaca". Then, we remove "aaa" to get "ca".
# Input: s = "abbaccaa", k = 3
# Output: "abbaccaa"
# Explanation: There are no instances of 3 adjacent characters being the same.
# Input: s = "abbacccaa", k = 3
# Output: "abb"
# Explanation: First, we remove "ccc" to get "abbaaa". Then, we remove "aaa" to get "abb".


# This problem can be solved by using a stack to keep track of the characters and their counts. We iterate through the string and add each character and its count to the stack. If the count of the top character of the stack becomes k, we remove that entry from the stack. The result string is then constructed from the remaining characters in the stack.


class Solution:
    def removeDuplicates(self, s:str, k:int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()
        
        return ''.join(c * n for c, n in stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("abbbaaca", 3))  # Output: "ca"
    print(solution.removeDuplicates("abbaccaa", 3))  # Output: "abbaccaa"
    print(solution.removeDuplicates("abbacccaa", 3))  # Output: "abbaa"

# The time complexity of this algorithm is O(N), where N is the length of s, as we perform one operation per character. The space complexity is also O(N), as in the worst case, all characters are pushed onto the stack.