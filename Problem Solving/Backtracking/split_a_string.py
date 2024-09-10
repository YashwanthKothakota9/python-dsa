# Given a string s, return the maximum number of unique substrings that the given string can be split into.

# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "aab"
# Output: 2
# Explanation: Two possible ways to split the given string into maximum unique substrings are: ['a', 'ab'] & ['aa', 'b'], both have 2 substrings; hence the maximum number of unique substrings in which the given string can be split is 2.
# Example 2:

# Input: s = "abcabc"
# Output: 4
# Explanation: Four possible ways to split into maximum unique substrings are: ['a', 'b', 'c', 'abc'] & ['a', 'b', 'cab', 'c'] &  ['a', 'bca', 'b', 'c'] & ['abc', 'a', 'b', 'c'], all have 4 substrings.


# We can use backtracking to solve this problem.

# This solution uses a helper function splitAndCount which takes three arguments, the input string s, the current start position and a set set to keep track of the unique substrings that have been split so far. The maxUniqueSplit function calls the splitAndCount function to find the maximum number of unique substrings that the given string can be split into.

# The splitAndCount function starts with a base case where it returns the size of the set when the current start position is equal to the length of the input string. This means that all substrings have been processed and the size of the set represents the maximum number of unique substrings.

# The function then uses a for loop to iterate through all possible substrings starting from the current start position. For each substring, it checks if the substring is already in the set. If it is not, the substring is added to the set and the function is recursively called with the new start position being the end of the current substring. This continues until all possible substrings have been processed.

# After the recursive call, the substring is removed from the set to backtrack. The function keeps track of the maximum number of unique substrings found so far and returns this maximum count when all substrings have been processed.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.split_and_count(s, 0, set())

    def split_and_count(self, s: str, start: int, set) -> int:
        # base case, if we have reached the end of the input string, return the size of the set
        if start == len(s):
            return len(set)

        count = 0
        # loop through all substrings starting from the current start position
        for i in range(start+1, len(s)+1):
            string = s[start:i]
            # if the substring is not in the set, add it and recursively call the function with the new start position
            if string not in set:
                set.add(string)
                count = max(count, self.split_and_count(s, i, set))
                # remove the substring from the set and backtrack
                set.remove(string)

        return count


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    input1 = "abcabc"
    output1 = sol.maxUniqueSplit(input1)
    print("maxUniqueSplit(" + input1 + ") = " + str(output1))  # Expected: 4

    # Test Case 2
    input2 = "aab"
    output2 = sol.maxUniqueSplit(input2)
    print("maxUniqueSplit(" + input2 + ") = " + str(output2))  # Expected: 2

    # Test Case 3
    input3 = "ababab"
    output3 = sol.maxUniqueSplit(input3)
    print("maxUniqueSplit(" + input3 + ") = " + str(output3))  # Expected: 4

    # Test Case 4
    input4 = ""
    output4 = sol.maxUniqueSplit(input4)
    print("maxUniqueSplit(" + input4 + ") = " + str(output4))  # Expected: 0

    # Test Case 5
    input5 = "a"
    output5 = sol.maxUniqueSplit(input5)
    print("maxUniqueSplit(" + input5 + ") = " + str(output5))  # Expected: 1


# Time Complexity
# We can split any given string of length n in 2^n ways. Hence the time complexity will be O(2^n).

# Space Complexity
# The space complexity will be O(n) as we need to save only one way of splitting the given string while in the recursion, and our recursion tree won't get bigger than O(n) steps too.
