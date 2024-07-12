class Solution:
    def countFreq(self, arr, key):
        return self.countFreqHelper(arr, key, 0)
    
    def countFreqHelper(self, arr, key, index):
        if index >= len(arr):
            return 0
        count = 1 if arr[index] == key else 0
        total_count = count + self.countFreqHelper(arr,key,index+1)
        return total_count

sol = Solution()
arr1 = [2, 4, 6, 8, 4]
key1 = 4
print("Occurrences in arr1:", sol.countFreq(arr1, key1))

arr2 = [1, 3, 5, 7, 9]
key2 = 2
print("Occurrences in arr2:", sol.countFreq(arr2, key2))

arr3 = [1, 2, 2, 2, 3]
key3 = 2
print("Occurrences in arr3:", sol.countFreq(arr3, key3))
