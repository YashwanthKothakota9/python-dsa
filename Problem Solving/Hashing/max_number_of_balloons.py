# Given a string, determine the maximum number of times the word "balloon" can be formed using the characters from the string. Each character in the string can be used only once.

# Examples:

# Example 1:

# Input: "balloonballoon"
# Expected Output: 2
# Justification: The word "balloon" can be formed twice from the given string.
# Example 2:

# Input: "bbaall"
# Expected Output: 0
# Justification: The word "balloon" cannot be formed from the given string as we are missing the character 'o' twice.


# To solve this problem, you start by creating a hashmap to count the frequency of each letter in the given string. Since the word "balloon" contains specific letters with varying frequencies (like 'l' and 'o' appearing twice), you need to account for these in your hashmap. Once you have the frequency of each letter, the next step is to determine how many times you can form the word "balloon". This is done by finding the minimum number of times each letter in "balloon" appears in the hashmap. The limiting factor will be the letter with the minimum frequency ratio to its requirement in the word "balloon". This approach ensures a balance between utilizing the available letters and adhering to the letter composition of "balloon".

from collections import defaultdict

class Solution:
    def maxNumOfBalloons(self, text:str) -> int:
        char_count = defaultdict(int)
        
        for ch in text:
            char_count[ch] += 1
        
        min_count = float('inf')
        
        min_count = min(min_count, char_count['b'])
        min_count = min(min_count, char_count['a'])
        min_count = min(min_count, char_count['l'] // 2)
        min_count = min(min_count, char_count['o'] // 2)
        min_count = min(min_count, char_count['n'])
        
        return min_count # type: ignore

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumOfBalloons("balloonballoon"))  # Expected: 2
    print(sol.maxNumOfBalloons("bbaall"))          # Expected: 0
    print(sol.maxNumOfBalloons("balloonballoooon")) # Expected: 2


# Tc: O(n) Sc: O(1)