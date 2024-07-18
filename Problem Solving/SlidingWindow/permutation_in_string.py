# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters, it will have n! permutations.

# Example 1:

# Input: str="oidbcaf", pattern="abc"   
# Output: true   
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: str="odicf", pattern="dc"   
# Output: false  
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: str="bcdxabcdy", pattern="bcdyabcdx"  
# Output: true  
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: str="aaacb", pattern="abc"  
# Output: true  
# Explanation: The string contains "acb" which is a permutation of the given pattern.

# To solve this problem, we use a sliding window technique combined with a hashmap to keep track of character frequencies. The sliding window allows us to check each substring of the input string efficiently. The hashmap stores the count of each character in the pattern. As we slide the window over the string, we compare the character counts of the current window with those in the hashmap. This approach ensures that we only check substrings that are the same length as the pattern, which makes it very efficient.

# The reason this approach is effective is due to its linear time complexity. Instead of generating all possible substrings, we slide a window of fixed size across the string and update our counts dynamically. This reduces the number of comparisons and allows us to quickly determine if a permutation of the pattern exists in the string. It is the most efficient approach as it combines the benefits of the sliding window and hashmap for constant time lookups and updates.


# Time Complexity
# The above algorithm’s time complexity will be O(N+M), where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.

# Space Complexity
# The algorithm’s space complexity is O(M) since, in the worst case, the whole pattern can have distinct characters that will go into the HashMap.

class Solution:
    def findPermutation(self, str1, pattern):
        window_start, matched = 0, 0
        freq_map = {}
        
        for ch in pattern:
            if ch not in freq_map:
                freq_map[ch] = 0
            freq_map[ch] += 1
        
        print(f"FreqMap Before sliding window: {freq_map}")
        # our goal is to match all the characters from the 'char_frequency' with the current
        # window try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            print(f"RightChar: {right_char}")
            if right_char in freq_map:
                # decrement the frequency of matched character
                freq_map[right_char] -= 1
                if freq_map[right_char] == 0:
                    matched += 1
            
            print(f"matched: {matched}")
            if matched == len(freq_map):
                return True
            
            # shrink the window by one character
            if window_end >= len(pattern)-1:
                left_char = str1[window_start]
                print(f"LeftChar: {left_char}")
                window_start += 1
                if left_char in freq_map:
                    if freq_map[left_char] == 0:
                        matched -= 1
                    freq_map[left_char] += 1
            print(f"FreqMap in sliding window: {freq_map}")
        return False

def main():
    sol = Solution()
    print('Permutation exist: ' + str(sol.findPermutation("oidbcaf", "abc")))
    # print('Permutation exist: ' + str(sol.findPermutation("odicf", "dc")))
    # print('Permutation exist: ' + str(sol.findPermutation("bcdxabcdy", "bcdyabcdx")))
    # print('Permutation exist: ' + str(sol.findPermutation("aaacb", "abc")))


main()