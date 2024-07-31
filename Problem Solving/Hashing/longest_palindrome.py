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


# To solve this problem, we can use a hashmap to keep track of the frequency of each character in the string. The idea is to use pairs of characters to form the palindrome. For example, if a character appears an even number of times, we can use all of them in the palindrome. If a character appears an odd number of times, we can use all except one of them in the palindrome. Additionally, if there's any character that appears an odd number of times, we can use one of them as the center of the palindrome.


from collections import Counter


class Solution:
    def longestPalindrome(self, s:str) -> int:
        freq_map = Counter(s)
        length = 0
        oddFound = False
        for freq in freq_map.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq-1
                oddFound = True
        if oddFound:
            length += 1
        return length

sol = Solution()
print(sol.longestPalindrome("bananas"))   # Expected output: 5
print(sol.longestPalindrome("applepie"))  # Expected output: 7
print(sol.longestPalindrome("racecar"))   # Expected output: 7


# Time Complexity:
# Iterating through the string: We iterate through the entire string once to count the frequency of each character. This operation takes (O(n)) time, where (n) is the length of the string.

# Iterating through the hashmap: After counting the frequencies, we iterate through the hashmap to determine how many characters can be used to form the palindrome. In the worst case, this would be (O(26)) for the English alphabet, which is a constant time. However, in general terms, if we consider any possible character (not just English alphabet), this would be (O(k)), where (k) is the number of unique characters in the string.

# Combining the two steps, the overall time complexity is (O(n) + O(k) = O(n)) as k<= n .

# Space Complexity:
# Hashmap for character frequencies: The space taken by the hashmap is proportional to the number of unique characters in the string. In the worst case, this would be (O(26)) for the English alphabet, which is a constant space. However, in general terms, if we consider any possible character (not just English alphabet), this would be (O(k)), where (k) is the number of unique characters in the string.

# Thus, the space complexity of the algorithm is (O(1)).