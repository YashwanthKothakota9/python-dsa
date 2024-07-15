class Solution:
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)-1]
        smaller, equal, larger = [], [], []
        
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        
        return self.sort(smaller) + equal + self.sort(larger)


sol = Solution()
examples = [
    [4, 2, 6, 8, 3],
    [10, 5, 3, 7, 2, 8, 6],
    [1, 2, 3, 4, 5]
]

for i, array in enumerate(examples):
    sortedArray = sol.sort(array)
    print(f"Sorted Array #{i + 1}: {sortedArray}")