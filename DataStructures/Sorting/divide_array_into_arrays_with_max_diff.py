# You are given an array nums containing n integers and a positive integer k.

# Divide the nums into arrays of size 3 such that it satisfies the below conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements of a single array should be less than or equal to k.
# Return a 2D array of these subarrays. If no such division is possible, return an empty array.

# Example 1:

# Input: nums = [2, 6, 4, 9, 3, 7, 3, 4, 1], k = 3
# Expected Output: [[1,2,3],[3,4,4],[6,7,9]]
# Explanation: The three groups [1, 2, 3], [3, 4, 4] and [6, 7, 9] all have elements with differences ≤ k. For the group [1, 2, 3] the maximum difference between elements is 2. For the group [3, 4, 4], the maximum difference is 1, and for [6, 7, 9], it's 3, all of which satisfy the condition.
# Example 2:

# Input: nums = [10, 12, 15, 20, 25, 30], k = 10
# Expected Output: [[10, 12, 15], [20, 25, 30]]
# Explanation: Here, the two groups have maximum differences of 5 and 10 respectively, which are less than or equal to k, thus meeting the criteria perfectly.
# Example 3:

# Input: nums = [1, 2, 4, 5, 9, 10], k = 1
# Expected Output: []
# Explanation: It is not possible to divide the nums in subarrays as the value of the k is equal to 1.


# To solve this problem, we will first sort the array to ensure that elements that are close to each other numerically are also close in index. This sorting will make it easier to find subarrays where the difference between the maximum and minimum values does not exceed k.

# After sorting, we'll iterate over the array and group every three consecutive elements into a subarray, checking if they satisfy the condition. This approach is effective because sorting brings elements with smaller differences together, which simplifies the process of forming the required subarrays. By processing every three elements as a group, we ensure each group is checked for the condition independently.

class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        result = []
        
        # Iterate over the array in steps of 3 since each subarray must contain exactly 3 elements
        for i in range(0, len(nums)-2,3):
            # Check if the max difference within the current triplet is within the allowed limit k
            print(i)
            if(nums[i+2] - nums[i]) <= k:
                subgroup = [nums[i],nums[i+1],nums[i+2]]
                result.append(subgroup)
            else:
                return []
        
        return result

sol = Solution()

# Example 1
nums1 = [2, 6, 4, 9, 3, 7, 3, 4, 1]
k1 = 3
print("Example 1 Output:", sol.divideArray(nums1, k1))

# Example 2
nums2 = [10, 12, 15, 20, 25, 30]
k2 = 10
print("Example 2 Output:", sol.divideArray(nums2, k2))

# Example 3
nums3 = [1, 2, 4, 5, 9, 10]
k3 = 2
print("Example 3 Output:", sol.divideArray(nums3, k3))
