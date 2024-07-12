class Solution:
    
    def isVowel(self, ch):
        return ch in "aeiouAEIOU"
    
    def countingSortVowels(self, s):
        freqMap = {}
        for ch in s:
            if self.isVowel(ch):
                freqMap[ch] = freqMap.get(ch,0) + 1
        
        sortedVowelOrder = "AEIOUaeiou"
        result = ""
        index = 0
        
        for ch in s:
            if not self.isVowel(ch):
                result += ch
            else:
                while index < len(sortedVowelOrder) and freqMap.get(sortedVowelOrder[index],0) == 0:
                    index += 1
                
                if index < len(sortedVowelOrder):
                    result += sortedVowelOrder[index]
                    freqMap[sortedVowelOrder[index]] -= 1
        return result

solution = Solution()
print(solution.countingSortVowels("gamE"))      # gEma
print(solution.countingSortVowels("aEiOu"))     # Eoaiu
print(solution.countingSortVowels("DesIgnGurUs"))# DIsUgnGerus
print(solution.countingSortVowels("Yashwanth"))