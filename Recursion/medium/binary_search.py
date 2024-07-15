class Solution:
    def binarySearch(self, nums, target):
        return self.binarySearchHelper(nums, target, 0, len(nums)-1)
    
    def binarySearchHelper(self, nums, target, low, high):
        if low > high:
            return False
        
        mid = low + (high - low)//2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.binarySearchHelper(nums, target, low, mid-1)
        else:
            return self.binarySearchHelper(nums, target, mid+1, high)

sol = Solution()
examples = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15]
]
keys = [4, 5, 15]

for i in range(len(examples)):
    nums = examples[i]
    target = keys[i]
    result = sol.binarySearch(nums, target)
    print(f"Example {i + 1}: {target} found? {result}")