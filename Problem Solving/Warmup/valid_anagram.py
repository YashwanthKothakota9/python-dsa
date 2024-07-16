# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "listen", t = "silent"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Example 3:

# Input: s = "hello", t = "world"
# Output: false

# Tc: O(n) Sc: O(1)

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_map = {}
        for i in range(len(s)):
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1
            
            if t[i] in freq_map:
                freq_map[t[i]] -= 1
            else:
                freq_map[t[i]] = -1
            
        for ch in freq_map:
            if freq_map[ch] != 0:
                return False
    
        return True

sol = Solution()
# Test case 1
s1 = "listen"
t1 = "silent"
print(sol.isAnagram(s1, t1))  # Expected output: True

# Test case 2
s2 = "hello"
t2 = "world"
print(sol.isAnagram(s2, t2))  # Expected output: False

# Test case 3
s3 = "anagram"
t3 = "nagaram"
print(sol.isAnagram(s3, t3))  # Expected output: True

# Test case 4
s4 = "rat"
t4 = "car"
print(sol.isAnagram(s4, t4))  # Expected output: False

# Test case 5
s5 = ""
t5 = ""
print(sol.isAnagram(s5, t5))  # Expected output: True
