# Given a list of strings, the task is to group the anagrams together.

# An anagram is a word or phrase formed by rearranging the letters of another, such as "cinema", formed from "iceman"

# You can return the answer in any order.

# Examples
# Example 1:
# Input: ["dog", "god", "hello"]
# Output: [["dog", "god"], ["hello"]]
# Justification: "dog" and "god" are anagrams, so they are grouped together. "hello" does not have any anagrams in the list, so it is in its own group.
# Example 2:
# Input: ["listen", "silent", "enlist"]
# Output: [["listen", "silent", "enlist"]]
# Justification: All three words are anagrams of each other, so they are grouped together.
# Example 3:
# Input: ["abc", "cab", "bca", "xyz", "zxy"]
# Output: [["abc", "cab", "bca"], ["xyz", "zxy"]]
# Justification: "abc", "cab", and "bca" are anagrams, as are "xyz" and "zxy".
# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Solution
# Sorting Approach:

# For each word in the input list:
# Sort the letters of the word.
# Use the sorted word as a key in a hash map, and add the original word to the list of values for that key.
# The hash map values will be the groups of anagrams.
# Why This Will Work:

# Anagrams will always result in the same sorted word, so they will be grouped together in the hash map.

# Complexity Analysis
# Time Complexity: O(n*k*log(k)), where n is the number of strings, and k is the maximum length of a string in strs. This is because each of the n strings is sorted in O(k*log(k)) time.
# Space Complexity: O(n*k), where n is the number of strings, and k is the maximum length of a string in strs. This space is used for the output data structure and the hash map.


class Solution:
    def group_anagrams(self, words):
        # Dictionary to hold sorted word as key and list of words as value
        d = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = []
            d[sorted_word].append(word)
        # print(d)
        # print(d.keys())
        return list(d.values())


sol = Solution()
print(sol.group_anagrams(["dog", "god", "hello"]))
print(sol.group_anagrams(["listen", "silent", "enlist"]))
print(sol.group_anagrams(["abc", "cab", "bca", "xyz", "zxy"]))
