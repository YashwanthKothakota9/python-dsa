# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:

# Input: str="ppqp", pattern="pq"  
# Output: [1, 2]  
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:

# Input: str="abbcabc", pattern="abc"  
# Output: [2, 3, 4]  
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


# To solve this problem, we use a sliding window approach along with a frequency map to keep track of character counts. By moving the window across the string, we can compare the current window's characters with the pattern's characters.

# This method is efficient because it allows us to check each possible window without repeatedly recalculating character counts from scratch. The sliding window approach is chosen because it ensures that each character in the string is processed only once, making the algorithm time-efficient. Moreover, using a hash map to store character frequencies helps quickly check if a window matches the pattern.


# Time Complexity

# The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

# Space Complexity

# The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.


class Solution:
    def findAnagrams(self, str1, pattern):
        window_start, matched = 0, 0
        freq_map = {}
        
        for ch in pattern:
            if ch not in freq_map:
                freq_map[ch] = 0
            freq_map[ch] += 1
        
        result_indices = []
        # Our goal is to match all the characters from the 'char_frequency' with the current
        # window try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in freq_map:
                # Decrement the frequency of matched character
                freq_map[right_char] -= 1
                if freq_map[right_char] == 0:
                    matched += 1
            
            if matched == len(freq_map):# Have we found an anagram?
                result_indices.append(window_start)
            
            # Shrink the sliding window
            if window_end >= len(pattern) - 1:
                left_char = str1[window_start]
                window_start += 1
                if left_char in freq_map:
                    if freq_map[left_char] == 0:
                        matched -= 1 # Before putting the character back, decrement the matched count
                    freq_map[left_char] += 1
        
        return result_indices

def main():
    sol = Solution()
    print(sol.findAnagrams("ppqp", "pq"))
    print(sol.findAnagrams("abbcabc", "abc"))


main()