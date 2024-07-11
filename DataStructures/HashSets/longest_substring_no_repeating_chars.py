# Given a string, identify the length of its longest segment that contains distinct characters. In other words, find the maximum length of a substring that has no repeating characters.

# Examples:

# Example 1:

# Input: "abcdaef"
# Expected Output: 6
# Justification: The longest segment with distinct characters is "bcdaef", which has a length of 6.
# Example 2:

# Input: "aaaaa"
# Expected Output: 1
# Justification: The entire string consists of the same character. Thus, the longest segment with unique characters is just "a", with a length of 1.
# Example 3:

# Input: "abrkaabcdefghijjxxx"
# Expected Output: 10
# Justification: The longest segment with distinct characters is "abcdefghij", which has a length of 10.

# To solve the problem, iterate through the characters of the given string while maintaining a HashSet to track the characters already encountered. As we traverse the string, each character is checked against the HashSet. If the character is not present in the HashSet, it indicates no repetition, and we add it to the HashSet and continue. However, if a character is already in the HashSet, it means a repetition has occurred. At this point, we update the length of the longest substring found so far (if necessary), and modify the HashSet to remove the characters up to and including the repeated character. This process continues until we have traversed the entire string. The final result is the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        char_set = set()
        maxLength, start, end = 0, 0, 0
        
        while end < len(s):
            # print(char_set)
            if s[end] not in char_set:
                char_set.add(s[end])
                maxLength = max(maxLength, end-start+1)
                end += 1
            else:
                char_set.remove(s[start])
                start += 1
        
        return maxLength
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcdaef"))       # Expected: 6
    print(sol.lengthOfLongestSubstring("aaaaa"))         # Expected: 1
    print(sol.lengthOfLongestSubstring("abrkaabcdefghijjxxx")) # Expected: 10
