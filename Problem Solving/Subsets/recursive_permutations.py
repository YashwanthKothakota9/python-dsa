class Solution:
    def generate_permutations(self, nums):
        result = []
        self.generate_permutations_recursive(nums, 0, [], result)
        return result
    
    def generate_permutations_recursive(self, nums, index, currentPermutation, result):
        if index == len(nums):
            result.append(currentPermutation)
        else:
            # create a new permutation by adding the current number at every position
            for i in range(len(currentPermutation)+1):
                new_permutation = list(currentPermutation)
                new_permutation.insert(i, nums[index])
                self.generate_permutations_recursive(nums, index+1, new_permutation, result)

def main():
  sol = Solution()
  print("Here are all the permutations: " + str(sol.generate_permutations([1, 3, 5])))


main()