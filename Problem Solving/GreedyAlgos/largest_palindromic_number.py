# Given a string s containing 0 to 9 digits, create the largest possible palindromic number using the string characters. It should not contain leading zeroes.

# A palindromic number reads the same backward as forward.

# If it's not possible to form such a number using all digits of the given string, you can skip some of them.

# Input: "323211444"
# Expected Output: "432141234"
# Justification: This is the largest palindromic number that can be formed from the given digits.

# Input: "998877"
# Expected Output: "987789"
# Justification: "987789" is the largest palindrome that can be formed.

# Input: "54321"
# Expected Output: "5"
# Justification: Only "5" can form a valid palindromic number as other digits cannot be paired.


# To solve this problem, the goal is to create the largest palindromic number possible using the digits from the given input number. A palindrome reads the same backward as forward, so our approach is to build the number symmetrically.

# First, we count the frequency of each digit in the input number using an array of size 10 (for digits 0-9). Then, we construct the first half of the palindrome by appending each digit as many times as half of its frequency, starting from the highest digit (9) down to the lowest (0). If there is a digit with an odd frequency, we select the largest such digit to be the center of the palindrome. Finally, we append the reversed first half to the original first half (with the center digit, if any) to complete the palindrome. This ensures that the number is the largest possible palindrome.


class Solution:
    def largestPalindromic(self, num:str) -> str:
        firstHalf = [] # List to store first half of the palindrome
        freq = [0] * 10 # Frequency array for digits 0-9
        
        # Count the frequency of each digit in the input number
        for ch in num:
            val = int(ch)
            freq[val] += 1
        
        middle = -1 # Variable to store the middle digit if needed
        
        # Iterate from the highest digit (9) to the lowest (0)
        for i in range(9, -1, -1):
            if freq[i] != 0 and (i!=0 or firstHalf):
                count = freq[i]
                while count > 1:
                    firstHalf.append(str(i)) # Append the digit to firstHalf
                    count -= 2 # Use two of the digit for the first half
                if count == 1 and middle == -1:
                    middle = i # Assign the middle digit if it's the largest odd-count digit
        
        secondHalf = firstHalf[::-1] # Create secondHalf as a reversed copy of firstHalf
        if middle != -1:
            firstHalf.append(str(middle)) # Append the middle digit if it exists
        firstHalf.extend(secondHalf) # Append the reversed first half to firstHalf
        
        return ''.join(firstHalf) if firstHalf else "0"


solution = Solution()
print(solution.largestPalindromic("323211444"))  # 432141234
print(solution.largestPalindromic("998877"))      # 987789
print(solution.largestPalindromic("54321"))       # 5


# Time Complexity: O(n), where n is the length of the input string. The algorithm involves iterating over the input string once for frequency counting and then iterating over the frequency array (constant size of 10).

# Space Complexity: Space Complexity: O(n), where (n) is the length of the input string.

# Frequency Array: O(10)~O(1) space.
# First Half StringBuilder: Up to O(n) space in the worst case.
# Middle String:O(1)  space.
        
                    
        