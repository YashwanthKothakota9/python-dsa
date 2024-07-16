# Given a string sentence containing English letters (lower- or upper-case), return true if sentence is a Pangram, or false otherwise.

# A Pangram is a sentence where every letter of the English alphabet appears at least once.

# Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.





from typing import Set


class Solution:
    def checkIfPangram(self, sentence:str) -> bool:
        seen: Set[str] = set()
        
        for char in sentence.lower():
            if char.isalpha():
                seen.add(char)
        
        return len(seen) == 26

sol = Solution()
# Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
# Expected output: True
print(sol.checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

# Test case 2: "This is not a pangram"
# Expected output: False
print(sol.checkIfPangram("This is not a pangram"))

# Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
# Expected output: True
print(sol.checkIfPangram("abcdef ghijkl mnopqr stuvwxyz"))

# Test case 4: ""
# Expected output: False
print(sol.checkIfPangram(""))

# Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Expected output: True
print(sol.checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
