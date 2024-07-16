# Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

# Example 1:

# Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
# Output: 5
# Explanation: The distance between "fox" and "dog" is 5 words.
# Example 2:

# Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
# Output: 1
# Explanation: The shortest distance between "a" and "b" is 1 word. Please note that "a" appeared twice.
# Example 3:

# Input: words = ["a", "b", "c", "d", "e"], word1 = "a", word2 = "e"
# Output: 4
# Explanation: The distance between "a" and "e" is 4 words

# To find the shortest distance between two given words, we can iterate through the list of words and use two pointers to track the positions of these words. Whenever we find one of these words in the list, we will update the word's position and calculate the distance from the other word. This way, we will keep track of the shortest distance between the two words.

# Tc: O(n) Sc: O(1)

class Solution:
    def shortestDistance(self, words, word1, word2):
        short_dist = len(words)
        position1, position2 = -1, -1
        
        for i, word in enumerate(words):
            if word == word1:
                position1 = i
            elif word == word2:
                position2 = i
            if position1 != -1 and position2 != -1:
                short_dist = min(short_dist, abs(position1 - position2))
        
        return short_dist


if __name__ == "__main__":
  solution = Solution()

  # Test case 1
  words1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
  word11 = "fox"
  word21 = "dog"
  expected_output1 = 5
  actual_output1 = solution.shortestDistance(words1, word11, word21)
  print("Test case 1:", expected_output1 == actual_output1)

  # Test case 2
  words2 = ["a", "b", "c", "d", "a", "b"]
  word12 = "a"
  word22 = "b"
  expected_output2 = 1
  actual_output2 = solution.shortestDistance(words2, word12, word22)
  print("Test case 2:", expected_output2 == actual_output2)

  # Test case 3
  words3 = ["a", "c", "d", "b", "a"]
  word13 = "a"
  word23 = "b"
  expected_output3 = 1
  actual_output3 = solution.shortestDistance(words3, word13, word23)
  print("Test case 3:", expected_output3 == actual_output3)

  # Test case 4
  words4 = ["a", "b", "c", "d", "e"]
  word14 = "a"
  word24 = "e"
  expected_output4 = 4
  actual_output4 = solution.shortestDistance(words4, word14, word24)
  print("Test case 4:", expected_output4 == actual_output4)    
