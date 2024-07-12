# Given a string, arrange its characters in descending order based on the frequency of each character. If two characters have the same frequency, their relative order in the output string can be arbitrary.

# Example
# Input: "apple"
# Expected Output: "ppale" or "ppela"
# Justification: The character 'p' appears twice, while 'a', 'l', and 'e' each appear once. Thus, 'p' should appear before the other characters in the output.
# Input: "banana"
# Expected Output: "aaannb".
# Justification: The character 'a' appears three times, 'n' twice and 'b' once.
# Input: "aabb"
# Expected Output: "aabb" or "bbaa"
# Justification: Both 'a' and 'b' appear twice, so they can appear in any order in the output.

import heapq
from collections import Counter

class Solution:
    def freqSort(self, s:str) -> str:
        freq_map = Counter(s)
        max_heap = [(-freq,char) for char,freq in freq_map.items()]
        heapq.heapify(max_heap)
        
        res = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char * (-freq))
        
        return ''.join(res)
    
sol = Solution()
print(sol.freqSort("programming")) # Expected: gggrrmmiapo
print(sol.freqSort("aab"))         # Expected: aab or baa
print(sol.freqSort("apple"))       # Expected: pplea
