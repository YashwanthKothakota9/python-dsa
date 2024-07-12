# Given a string str, return the longest nice substring of a given string.

# A substring is considered nice if for every lowercase letter in the substring, its uppercase counterpart is also present, and vice versa.

# If no such string exists, return an empty string.

# Examples
# Example 1:

# Input: "BbCcXxY"
# Expected Output: "BbCcXx"
# Justification: Here, "BbCcXx" is the longest substring where each letter's uppercase and lowercase forms are present.
# Example 2:

# Input: "aZAbcD"
# Expected Output: ""
# Justification: There is no contiguous substring where each character exists in both its uppercase and lowercase forms.
# Example 3:

# Input: "qQwWeErR"
# Expected Output: "qQwWeErR"
# Justification: The entire string is the longest nice substring since every letter exists in both uppercase and lowercase forms.

# To solve this problem, you can use a straightforward approach. First, check if the entire string is 'nice', which means it has each letter in both uppercase and lowercase. If it's not, then you start breaking the string into smaller parts. You do this by dividing the string around each character, creating two new segments each time: one on the left and one on the right of that character.

# This splitting helps you explore every possible combination to find a 'nice' substring. For each of these smaller strings, you apply the same 'nice' criteria. If a substring qualifies, compare its length with your current longest 'nice' substring and keep the longer one. Continue this process of dividing and checking each part of the string.

# Through this method, you ensure that no potential 'nice' substring is missed.

class Solution:
    @staticmethod
    def isNice(s):
        charMap = [0]*128
        
        for c in s:
            charMap[ord(c)] += 1
        
        for c in s:
            if( c.islower() and charMap[ord(c.upper())]==0) or (c.isupper() and charMap[ord(c.lower())]==0):
                return False
        return True
    
    def findLongestNiceSubstring(self,s):
        if s is None or len(s) <= 1:
            return ""
        if Solution.isNice(s):
            return s
        longest = ""
        for i in range(len(s)):
            left = s[:i]
            right = s[i+1:]
            
            left_nice = self.findLongestNiceSubstring(left)
            right_nice = self.findLongestNiceSubstring(right)
            
            if len(left_nice) >= len(right_nice):
                if len(left_nice) > len(longest):
                    longest = left_nice
            else:
                if len(right_nice) > len(longest):
                    longest = right_nice
        return longest
    
sol = Solution()
print(sol.findLongestNiceSubstring("BbCcXxY"))  # Expected: BbCcXx
print(sol.findLongestNiceSubstring("aZAbcD"))   # Expected: (empty string)
print(sol.findLongestNiceSubstring("qQwWeErR")) # Expected: qQwWeErR

# Tc: O(n^3) Sc: O(n)