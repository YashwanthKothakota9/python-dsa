# Given a string, determine the length of the longest palindrome that can be constructed using the characters from the string. Return the maximum possible length of the palindromic string.

# Examples:

# Input: "applepie"
# Expected Output: 5
# Justification: The longest palindrome that can be constructed from the string is "pepep", which has a length of 5. There are are other palindromes too but they all will be of length 5.
# Input: "aabbcc"
# Expected Output: 6
# Justification: We can form the palindrome "abccba" using the characters from the string, which has a length of 6.
# Input: "bananas"
# Expected Output: 5
# Justification: The longest palindrome that can be constructed from the string is "anana", which has a length of 5.


# Initialization: Start by initializing a hashmap to keep track of the characters and their frequencies.

# Character Counting: Iterate through the string and populate the hashmap with the frequency of each character.

# Palindrome Length Calculation: For each character in the hashmap, if it appears an even number of times, add its count to the palindrome length. If it appears an odd number of times, add its count minus one to the palindrome length. Also, set a flag indicating that there's a character available for the center of the palindrome.

# Final Adjustment: If the center flag is set, add one to the palindrome length.



from collections import Counter

class Solution:
    def longestPalindrome(self,s:str) -> int:
        # Get character frequencies
        freq_map = Counter(s)
        length = 0
        oddFound = False
        
        # Calculate the palindrome length
        for freq in freq_map.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq-1
                oddFound = True
        
        # Add the central character if any odd frequency was found
        if oddFound:
            length += 1
        
        return length
    
sol = Solution()
print(sol.longestPalindrome("bananas"))   # Expected output: 5
print(sol.longestPalindrome("applepie"))  # Expected output: 7
print(sol.longestPalindrome("racecar"))   # Expected output: 7
