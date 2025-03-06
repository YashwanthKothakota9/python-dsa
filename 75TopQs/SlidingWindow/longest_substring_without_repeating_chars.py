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

# Algorithm Description:

# To solve the problem, iterate through the characters of the given string while maintaining a HashSet to track the characters already encountered. As we traverse the string, each character is checked against the HashSet. If the character is not present in the HashSet, it indicates no repetition, and we add it to the HashSet and continue. However, if a character is already in the HashSet, it means a repetition has occurred. At this point, we update the length of the longest substring found so far (if necessary), and modify the HashSet to remove the characters up to and including the repeated character. This process continues until we have traversed the entire string. The final result is the length of the longest substring without repeating characters.

# Initialization: Begin with two pointers, start and end, both at the start of the string. The hashset will initially be empty.

# Sliding Window Expansion: Progressively move the end pointer to the right until you come across a character that's already in the hashset, indicating a repetition.

# Adjusting Start Pointer: Upon detecting a repeated character, increment the start pointer by one position and remove the character at the start position from the hashset. This action ensures that the window only contains unique characters.

# Result Calculation: At each step, calculate the length of the current window (from start to end). Keep track of the maximum length observed.

# By the end of this process, the maximum length observed will be the length of the longest segment of unique characters in the string.

# Time Complexity
# While Loop: The algorithm uses a sliding window approach with two pointers, start and end. In the worst-case scenario, both pointers traverse the entire length of the string. Since each pointer can move from the beginning to the end of the string, the time complexity is O(2n), where n is the length of the string. However, in big O notation, constants are dropped, so the time complexity is O(n).

# HashSet Operations: The operations of adding, deleting, and checking for the existence of an element in a HashSet (or Set in some languages) are O(1) on average. Therefore, these operations don't add any significant overhead to the time complexity.

# Combining the above points, the overall time complexity of the algorithm is O(n).

# Space Complexity
# HashSet: The space complexity is determined by the size of the HashSet. In the worst-case scenario, the HashSet will store all unique characters of the string. Since the set of possible characters is fixed (assuming the ASCII character set, which has 128 characters, or the extended ASCII set, which has 256 characters), the space complexity is O(min(n, m)), where n is the length of the string and m is the character set size (either 128 or 256). For most strings, n will be much larger than m, so the space complexity is effectively O(m), which is a constant.
# Therefore, the overall space complexity of the algorithm is O(1), as it's constant and does not grow with the size of the input string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        start = 0
        for end in range(len(s)):
            if s[end] not in char_set:
                char_set.add(s[end])
                max_length = max(max_length, end-start+1)
            else:
                char_set.remove(s[start])
                start += 1
        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcdaef"))       # Expected: 6
    print(sol.lengthOfLongestSubstring("aaaaa"))         # Expected: 1
    print(sol.lengthOfLongestSubstring("abrkaabcdefghijjxxx"))  # Expected: 10
