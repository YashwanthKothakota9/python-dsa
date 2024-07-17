# Tc: O(N^3) Sc: O(N)

class Solution:
    def tripletSearch(self, arr, target):
        arr.sort()
        triplets = []
        for i in range(len(arr)-2):
            self.searchPair(arr, target-arr[i], i, triplets)
        return triplets
    
    def searchPair(self, arr, targetSum, first, triplets):
        left, right = first+1, len(arr)-1
        while left < right:
            if arr[left] + arr[right] < targetSum:
                # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between left and right to get a sum less than the target sum
                for i in range(right, left, -1):
                    triplets.append([arr[first], arr[left], arr[i]])
                left += 1
            else:
                right -= 1

def main():
  sol = Solution()
  print(sol.tripletSearch([-1, 0, 2, 3], 3))
  print(sol.tripletSearch([-1, 4, 2, 1, 3], 5))


main()
