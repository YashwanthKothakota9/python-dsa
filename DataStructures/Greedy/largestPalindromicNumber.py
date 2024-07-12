# Given a string s containing 0 to 9 digits, create the largest possible palindromic number using the string characters.

# A palindromic number reads the same backward as forward.

# If it's not possible to form such a number using all digits of the given string, you can skip some of them.

# Examples
# Input: "323211444"
# Expected Output: "432141234"
# Justification: This is the largest palindromic number that can be formed from the given digits.
# Input: "998877"
# Expected Output: "987789"
# Justification: "987789" is the largest palindrome that can be formed.
# Input: "54321"
# Expected Output: "5"
# Justification: Only "5" can form a valid palindromic number as other digits cannot be paired.


# To solve this problem, begin by counting the frequency of each character in the provided string.

# Next, construct the palindrome in two halves. Start with the first half: for each digit, use half of its total occurrences and add digits in descending order. If a digit occurs an odd number of times, set aside one occurrence for the middle of the palindrome. The middle element should be the largest digit that appears an odd number of times. Once the first half is complete, replicate it in reverse order to form the second half.

# In cases where there's no first half but there is a single digit with an odd count, use that digit as the palindrome. If it's not possible to form any palindrome, return "0".

class Solution:
    def largestPalindrome(self, num: str) -> str:
        freq = [0]*10
        for digit in num:
            freq[int(digit)] += 1
        
        first_half,middle = [],''
        for i in range(9,-1,-1):
            if freq[i]%2 != 0 and middle == '':
                middle = str(i)
            first_half.extend([str(i)] * (freq[i]//2))
        
        if not first_half:
            return middle if middle else '0'
        elif all(d=='0' for d in first_half):
            return '0'
        
        return ''.join(first_half) + middle + ''.join(reversed(first_half))

solution = Solution()
print(solution.largestPalindrome("323211444"))  # 432141234
print(solution.largestPalindrome("998877"))     # 987789
print(solution.largestPalindrome("54321"))      # 5
