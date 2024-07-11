# Given two strings, one representing a ransom note and the another representing the available letters from a magazine, determine if it's possible to construct the ransom note using only the letters from the magazine. Each letter from the magazine can be used only once.

# Examples:

# Example 1:

# Input: Ransom Note = "hello", Magazine = "hellworld"
# Expected Output: true
# Justification: The word "hello" can be constructed from the letters in "hellworld".
# Example 2:

# Input: Ransom Note = "notes", Magazine = "stoned"
# Expected Output: true
# Justification: The word "notes" can be fully constructed from "stoned" from its first 5 letters.
# Example 3:

# Input: Ransom Note = "apple", Magazine = "pale"
# Expected Output: false
# Justification: The word "apple" cannot be constructed from "pale" as we are missing one 'p'.
# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


from collections import defaultdict
from typing import DefaultDict

class Solution:
    def canConstruct(self, ransomNote:str, magazine:str) -> bool:
        char_count:DefaultDict[str,int] = defaultdict(int)
        
        for char in magazine:
            char_count[char] += 1
        
        for char in ransomNote:
            if char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("hello", "hellworld"))  # Expected: true
    print(sol.canConstruct("notes", "stoned"))     # Expected: true
    print(sol.canConstruct("apple", "pale"))       # Expected: false
