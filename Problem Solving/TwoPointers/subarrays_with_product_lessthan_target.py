# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

# Example 1:

# Input: [2, 5, 3, 10], target=30                                              
# Output: [2], [5], [2, 5], [3], [5, 3], [10]                           
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:

# Input: [8, 2, 6, 5], target=50                                              
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]                         
# Explanation: There are seven contiguous subarrays whose product is less than the target.

# This problem follows the Sliding Window and the Two Pointers pattern and shares similarities with Triplets with Smaller Sum with two differences:

# In this problem, the input array is not sorted.
# Instead of finding triplets with sum less than a target, we need to find all subarrays having a product less than the target.

# TC:
# The main for-loop managing the sliding window takes O(N) but creating subarrays can take up to O(N^2) in the worst case. Therefore overall, our algorithm will take O(N^3).

# Sc:
# For an array with distinct elements, finding all of its contiguous subarrays is like finding the number of ways to choose two indices, i and j, in the array such that i <= j.

# If there are a total of n elements in the array, here is how we can count all the contiguous subarrays:

# When i = 0, j can have any value from 0 to n-1, giving a total of n choices.
# When i = 1, j can have any value from 1 to n-1, giving a total of n-1 choices.
# Similarly, when i = 2, j can have n-2 choices. … …
# When i = n-1, j can only have only 1 choice.
# Let’s combine all the choices:

# Which gives us a total of: n*(n+1)/2.

# So, at most, we need space for O(n^2)  output lists. At worst, each subarray can take  O(n) space, so overall, our algorithm’s space complexity will be O(n^3).


class Solution:
    def findSubarrays(self, arr, target):
        # Resultant list to store all valid subarrays.
        result = []
        product = 1.0
        # Left boundary of the current subarray.
        left = 0
        # Iterate over the array using 'right' as the right boundary of the current subarray.
        for right in range(len(arr)):
            # Update the product with the current element.
            product *= arr[right]
            # If the product is greater than or equal to the target, slide the left boundary to the right until product is less than target.
            while product >= target and left < len(arr):
                product /= arr[left]
                left += 1
            # Create a temporary list to store the current subarray.
            tempList = []
            # Iterate from 'right' to 'left' and add all these subarrays to the result.
            for i in range(right, left-1, -1):
                # Add the current element at the beginning of the list.
                tempList.insert(0, arr[i])
                print(f"TL: {tempList}")
                # Add the current subarray to the result.
                result.append(list(tempList))
                print(f"Res: {result}")
        return result
    
sol = Solution()
print(sol.findSubarrays([2, 5, 3, 10], 30))
print(sol.findSubarrays([8, 2, 6, 5], 50))