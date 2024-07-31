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


# To solve this problem, we will utilize a hashmap to keep track of the frequency of each character in the magazine. First, we iterate through the magazine, updating the hashmap with the count of each character. Then, we go through the ransom note. For each character in the note, we check if it exists in the hashmap and if its count is greater than zero. If it is, we decrease the count in the hashmap, indicating that we've used that letter. If at any point we find a character in the note that isn't available in sufficient quantity in the magazine, we return false. If we successfully go through the entire note without this issue, we return true, indicating the note can be constructed from the magazine.


from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote:str, magazine:str) -> bool:
        char_count = defaultdict(int)
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


# Time Complexity: The algorithm traverses both the ransom note and the magazine once, making the time complexity O(n + m), where n is the length of the ransom note and m is the length of the magazine.

# Space Complexity: The space complexity is determined by the hashmap, which in the worst case will have an entry for each unique character in the magazine. However, since the English alphabet has a fixed number of characters, the space complexity is O(1).