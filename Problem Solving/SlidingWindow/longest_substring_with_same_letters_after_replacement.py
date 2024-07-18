# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: str="aabccbb", k=2  
# Output: 5  
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: str="abbcb", k=1  
# Output: 4  
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: str="abccde", k=1  
# Output: 3  
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

# To solve this problem, we can use a sliding window technique. The idea is to maintain a window that can contain up to k characters that are different from the most frequent character in the current window. By doing so, we maximize the length of the window while keeping the number of changes within the allowed limit. This approach works because the window will only shrink when the number of characters that need to be changed exceeds k.

# The sliding window approach is efficient because it only requires a single pass through the string, making it suitable for handling large input sizes. Additionally, it uses a hashmap to keep track of the frequency of characters in the current window, ensuring that we can quickly determine the most frequent character. This combination of techniques ensures that the solution is both time and space efficient.


# Time Complexity
# The above algorithm’s time complexity will be O(N), where ‘N’ is the number of letters in the input string.

# Space Complexity

# As we expect only the lower case letters in the input string, we can conclude that the space complexity will be O(26) to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).

class Solution:
    def findLength(self, str1, k):
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        freq_map = {}
        # Try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in freq_map:
                freq_map[right_char] = 0
            freq_map[right_char] += 1
            
            max_repeat_letter_count = max(max_repeat_letter_count, freq_map[right_char])
            
            # Current window size is from window_start to window_end, overall we have a letter
            # which is repeating 'max_repeat_letter_count' times, this means we can have a window
            # which has one letter repeating 'max_repeat_letter_count' times and the remaining
            # letters we should replace. If the remaining letters are more than 'k', it is the
            # time to shrink the window as we are not allowed to replace more than 'k' letters
            if window_end - window_start + 1 - max_repeat_letter_count > k:
                left_char = str1[window_start]
                freq_map[left_char] -= 1
                window_start += 1
            
            print(f"FreqMap: {freq_map}")
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
    

def main():
    sol = Solution()
    print(sol.findLength("aabccbb", 2))
    print(sol.findLength("abbcb", 1))
    print(sol.findLength("abccde", 1))


main()