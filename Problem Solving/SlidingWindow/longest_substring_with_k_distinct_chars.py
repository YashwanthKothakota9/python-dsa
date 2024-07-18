# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# You can assume that K is less than or equal to the length of the given string.

# Example 1:
# Input: str="araaci", K=2  
# Output: 4  
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:
# Input: str="araaci", K=1  
# Output: 2  
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:
# Input: str="cbbebi", K=3  
# Output: 5  
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

# To solve this problem, we can use a sliding window approach. The idea is to maintain a window that contains at most ( K ) distinct characters. We will expand the window by including one character at a time from the right, and once the window contains more than ( K ) distinct characters, we will shrink it from the left until it again contains ( K ) or fewer distinct characters.

# This approach is effective because it allows us to process the string in linear time, which is efficient for large inputs. By keeping track of the frequency of characters within the window using a hash map, we can efficiently manage the characters and ensure that the window always contains at most ( K ) distinct characters.

# Tc: O(N) Sc: O(K)

class Solution:
    def findLength(self, str1, k):
        window_start = 0
        max_length = 0
        char_freq = {}
        # in the following loop we'll try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in char_freq:
                char_freq[right_char] = 0
            char_freq[right_char] += 1
            
            print(f"Len CharFreq: {len(char_freq)}, charFreq: {char_freq}")
            # shrink the sliding window, until we are left with 'k' distinct characters in
            # the char_frequency
            while len(char_freq) > k:
                left_char = str1[window_start]
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
    
def main():
    sol = Solution()
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 2)))
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 1)))
    print("Length of the longest substring: "
          + str(sol.findLength("cbbebi", 3)))


main()