class Solution:
    # Tc: O(N) Sc: O(N)
    def containsDuplicate(self,nums):
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False
    
    # Tc: O(NlogN) Sc: O(N)
    def containsDuplicate_sort(self,nums)->bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.containsDuplicate(nums1)) # Expected output: False
  print(sol.containsDuplicate_sort(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.containsDuplicate(nums2)) # Expected output: True
  print(sol.containsDuplicate_sort(nums2)) # Expected output: True

  nums3 = []
  print(sol.containsDuplicate(nums3)) # Expected output: False

  nums4 = [1, 1, 1, 1]
  print(sol.containsDuplicate(nums4)) # Expected output: True
