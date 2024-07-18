# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

# Example 1:

# Input: String="catfoxcat", Words=["cat", "fox"]  
# Output: [0, 3]  
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Example 2:

# Input: String="catcatfoxfox", Words=["cat", "fox"]  
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".

# To solve this problem, we need to check every possible starting position in the string where the concatenation of all given words might begin. We will use a sliding window approach. This approach involves creating a window of the size equal to the total length of all words combined and sliding it across the string, one character at a time. For each position of the window, we will check if it contains a valid concatenation of the given words. This method is effective because it reduces the number of unnecessary checks by focusing only on the relevant parts of the string.

# This approach is effective because it systematically checks all possible positions in the string, ensuring no potential concatenation is missed. By using a hashmap to store the frequency of each word in the list and another hashmap to track the words seen in the current window, we can efficiently validate the concatenations.


# Time Complexity
# The time complexity of the above algorithm will be O(N*M*Len) where ‘N’ is the number of characters in the given string, ‘M’ is the total number of words, and ‘Len’ is the length of a word.

# Space Complexity
# The space complexity of the algorithm is O(M) since, at most, we will be storing all the words in the two HashMaps. In the worst case, we also need O(N) space for the resulting list. So, the overall space complexity of the algorithm will be O(M+N).

class Solution:
    def findConcatenation(self, str1, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []
        
        word_freq = {}
        
        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1
        
        result_indices = []
        words_count = len(words)
        word_length = len(words[0])
        
        for i in range((len(str1) - words_count * word_length)+1):
            words_seen = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_length
                # Get the next word from the string
                word = str1[next_word_index: next_word_index + word_length]
                if word not in word_freq:  # Break if we don't need this word
                    break

                # Add the word to the 'words_seen' map
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1
                
                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_freq.get(word, 0):
                    break

                if j + 1 == words_count:  # Store index if we have found all the words
                    result_indices.append(i)
        return result_indices

def main():
    sol = Solution()
    print(sol.findConcatenation("catfoxcat", ["cat", "fox"]))
    print(sol.findConcatenation("catcatfoxfox", ["cat", "fox"]))


main()