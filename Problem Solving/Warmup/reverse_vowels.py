# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# We need to reverse the vowels in a string, keeping the positions of the consonants and other characters intact. We can use the two-pointer technique to traverse the string from both ends simultaneously. Whenever a vowel is encountered at both ends, we will swap them. The process will continue until the two pointers meet in the middle.

# Tc: O(n) Sc: O(n)

class Solution:
    
    vowels = "aeiouAEIOU"
    
    def reverseVowels(self, s: str) -> str:
        first , last  = 0, len(s)-1
        array = list(s)
        while first < last:
            while first < last and self.vowels.find(s[first]) == -1:
                first += 1
            
            while first < last and self.vowels.find(s[last]) == -1:
                last -= 1
            
            array[first], array[last] = array[last], array[first]
            
            first += 1
            last -= 1
        return "".join(array)


if __name__ == "__main__":
  solution = Solution()

  s1 = "hello"
  expected_output1 = "holle"
  actual_output1 = solution.reverseVowels(s1)
  print("Test Case 1: ", expected_output1 == actual_output1)

  s2 = "DesignGUrus"
  expected_output2 = "DusUgnGires"
  actual_output2 = solution.reverseVowels(s2)
  print("Test Case 2: ", expected_output2 == actual_output2)

  s3 = "AEIOU"
  expected_output3 = "UOIEA"
  actual_output3 = solution.reverseVowels(s3)
  print("Test Case 3: ", expected_output3 == actual_output3)

  s4 = "aA"
  expected_output4 = "Aa"
  actual_output4 = solution.reverseVowels(s4)
  print("Test Case 4: ", expected_output4 == actual_output4)

  s5 = ""
  expected_output5 = ""
  actual_output5 = solution.reverseVowels(s5)
  print("Test Case 5: ", expected_output5 == actual_output5)
