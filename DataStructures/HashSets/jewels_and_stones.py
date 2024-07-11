# Given two strings. The first string represents types of jewels, where each character is a unique type of jewel. The second string represents stones you have, where each character represents a type of stone. Determine how many of the stones you have are also jewels.

# Examples:

# Example 1:

# Input: Jewels = "abc", Stones = "aabbcc"
# Expected Output: 6
# Justification: All the stones are jewels.
# Example 2:

# Input: Jewels = "aA", Stones = "aAaZz"
# Expected Output: 3
# Justification: There are 2 'a' and 1 'A' stones that are jewels.
# Example 3:

# Input: Jewels = "zZ", Stones = "zZzZzZ"
# Expected Output: 6
# Justification: All the stones are jewels.

class Solution:
    def numJewelsInStones(self, jewels:str, stones:str) -> int:
        jewel_set = set(jewels)
        print(jewel_set)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("abc", "aabbcc"))  # Expected: 6
    print(sol.numJewelsInStones("aA", "aAaZz"))    # Expected: 3
    print(sol.numJewelsInStones("zZ", "zZzZzZ"))        # Expected: 6