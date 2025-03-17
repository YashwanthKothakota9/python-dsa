# Two strings are considered similar if you can make one string look like the other using the following two operations:

# Swap any two characters.
# For example, abde -> aedb (e and b swapped).
# Replace every occurrence of one character with another, and replace the other character with the first one.
# For example, acabbb -> bcbaaa (all a's turn into b's, and all b's turn into a's)
# Given two strings, word1 and word2, return true if they can be made similar, otherwise return false.

# Examples
# Example 1:

# Input: word1 = "aacbbc", word2 = "bbcaca"
# Expected Output: true
# Justification: You can swap the 'a's and 'b's in word2 to make it "aacbcb", then swap the last two characters to match word1.
# Example 2:

# Input: word1 = "xxyyzz", word2 = "zzxxyy"
# Expected Output: true
# Justification: Swapping characters 'x' with 'z' and then 'z' with 'y' in word2 will make it "xxyyzz", which matches word1.
# Example 3:

# Input: word1 = "aabbcc", word2 = "aabbc"
# Expected Output: false
# Justification: The lengths of the two strings are different, so they can't be made to look the same.

# Solution
# To solve this problem, the first step is to ensure that both strings have the same length. If they don't, they can't be made similar. Next, we need to check if both strings have the same set of characters. If one string has a character that the other doesn't, they can't be made to look the same. Lastly, we check the frequency of each character. Both strings must have the same frequency distribution of characters for them to be transformable into one another.

# This approach is effective because it simplifies the problem into three main checks: length, character set, and frequency distribution. By ensuring these conditions, we can determine if one string can be transformed into the other using the allowed operations.

# Complexity Analysis:
# Time Complexity
# The time complexity of this solution is O(n) where n is the length of the input strings. This is because we need to traverse the string. The sorting operation of count array takes constant time as its size is constant.

# Space Complexity
# The space complexity is O(1) because we are using fixed-size arrays (of size 26) and sets, and the extra space used does not depend on the input size.


class Solution:
    def close_strings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = [0]*26
        count2 = [0]*26

        set1 = set(word1)
        set2 = set(word2)

        for c in word1:
            count1[ord(c)-ord('a')] += 1

        for c in word2:
            count2[ord(c)-ord('a')] += 1

        count1.sort()
        count2.sort()

        return count1 == count2 and set1 == set2


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.close_strings("aacbbc", "bbcaca"))  # true

    # Example 2
    print(sol.close_strings("xxyyzz", "zzxxyy"))  # true

    # Example 3
    print(sol.close_strings("aabbcc", "aabbc"))  # false
