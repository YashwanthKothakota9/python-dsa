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
# Example 3:

# Input: "balloonballoooon"
# Expected Output: 2
# Justification: The word "balloon" can be formed twice, even though there are extra 'o' characters.
# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import defaultdict
from typing import DefaultDict

class Solution:
    def maxNoOfBalloons(self, text:str) -> int:
        char_count:DefaultDict[str,int] = defaultdict(int)
        for char in text:
            char_count[char] += 1
        min_count = min(
            char_count['b'],
            char_count['a'],
            char_count['l'] // 2,
            char_count['o'] // 2,
            char_count['n']
        )
        
        return min_count 

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNoOfBalloons("balloonballoon"))  # Expected: 2
    print(sol.maxNoOfBalloons("bbaall"))          # Expected: 0
    print(sol.maxNoOfBalloons("balloonballoooon")) # Expected: 2

