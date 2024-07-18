# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

# Example 1:

# Input: String="aabdec", Pattern="abc"  
# Output: "abdec"  
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:

# Input: String="aabdec", Pattern="abac"  
# Output: "aabdec"  
# Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"
# Example 3:

# Input: String="abdbca", Pattern="abc"  
# Output: "bca"  
# Explanation: The smallest substring having all characters of the pattern is "bca".
# Example 4:

# Input: String="adcad", Pattern="abc"  
# Output: ""  
# Explanation: No substring in the given string has all characters of the pattern

# To solve this problem, we use the sliding window technique. This approach helps us dynamically adjust the range of the substring we're considering. We start with two pointers, one at the beginning and another that expands to include new characters. As we move the right pointer to include characters, we check if the current window contains all the characters from pattern in the required frequency. Once it does, we try to shrink the window from the left to find the smallest possible window. This method is efficient because it avoids redundant calculations by reusing information from the previous state.

# This approach is effective because it ensures that each character in s is processed at most twice (once by each pointer), resulting in a linear time complexity relative to the length of s. The space complexity is manageable, as we only store the frequency of characters in a hash map. This guarantees that the solution is both time and space efficient.


# Time Complexity
# The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

# Space Complexity
# The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.

class Solution:
    def findSubstring(self, str1, pattern):
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(str1) + 1
        freq_map = {}
        
        for ch in pattern:
            if ch not in freq_map:
                freq_map[ch] = 0
            freq_map[ch] += 1
        
        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in freq_map:
                freq_map[right_char] -= 1
                if freq_map[right_char] >= 0:# Count every matching of a character
                    matched += 1
            
            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(pattern):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start
                
                left_char = str1[window_start]
                window_start += 1
                if left_char in freq_map:
                    # Note that we could have redundant matching characters, therefore we'll
                    # decrement the matched count only when a useful occurrence of a matched
                    # character is going out of the window
                    if freq_map[left_char] == 0:
                        matched -= 1
                    freq_map[left_char] += 1
        
        if min_length > len(str1):
            return ""
        
        return str1[substr_start:substr_start + min_length]
    

def main():
    sol = Solution()
    print(sol.findSubstring("aabdec", "abc"))
    print(sol.findSubstring("aabdec", "abac"))
    print(sol.findSubstring("abdbca", "abc"))
    print(sol.findSubstring("adcad", "abc"))


main()