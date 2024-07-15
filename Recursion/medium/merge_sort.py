from typing import List

class Solution:
    def mergeSort(self, arr:List[int]) -> List[int]:
        arr = self.mergeSortRecursive(arr)
        return arr
    
    def mergeSortRecursive(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        left_half = self.mergeSortRecursive(left_half)
        right_half = self.mergeSortRecursive(right_half)
        
        return self.merge(left_half, right_half)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged: List[int] = []
        i: int = 0
        j: int = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged

sol = Solution()
arr: List[int] = [5, 2, 8, 3, 1, 6]

print("Input Array:")
print(arr)

sorted_arr: List[int] = sol.mergeSort(arr)
print("Sorted Array: " + str(sorted_arr))