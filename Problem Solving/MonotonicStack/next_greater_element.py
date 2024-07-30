# Given two integer arrays nums1 and nums2, return an array answer such that answer[i] is the next greater number for every nums1[i] in nums2.

# The next greater element for an element x is the first element to the right of x that is greater than x. If there is no greater number, output -1 for that number.

# The numbers in nums1 are all present in nums2.

# Examples

# Input: nums1 = [4,2,6], nums2 = [6,2,4,5,3,7]
# Output: [5,4,7]
# Explanation: The next greater number for 4 is 5, for 2 is 4, and for 6 is 7 in nums2.
# Input: nums1 = [9,7,1], nums2 = [1,7,9,5,4,3]
# Output: [-1,9,7]
# Explanation: The next greater number for 9 does not exist, for 7 is 9, and for 1 is 7 in nums2.
# Input: nums1 = [5,12,3], nums2 = [12,3,5,4,10,15]
# Output: [10,15,5]
# Explanation: The next greater number for 5 is 10, for 12 is 15, and for 3 is 4 in nums2.


# This problem requires us to find the next greater element for each element in nums1 by searching nums2. The output array contains either the next greater element or -1 if no such element exists.

# This problem can be solved using a Monotonic Stack and Hashmap. The Monotonic Stack helps to find the next greater element for each element in nums2. The Hashmap then maps each element to its next greater element.


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, hashMap = [], {}
        for num in nums2:
            # Pop elements from the stack that are smaller than current number
            while stack and stack[-1] < num:
                hashMap[stack.pop()] = num# Remember the next greater element for num
            # Push current number onto stack
            stack.append(num)
        # Map the numbers in nums1 to their next greater number
        return [hashMap.get(num, -1) for num in nums1]

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,2,6]
    nums2 = [6,2,4,5,3,7]
    print(solution.nextGreaterElement(nums1, nums2))

# The time complexity of this algorithm is O(N), where N is the length of nums2, since each element is pushed and popped from the stack exactly once. The space complexity is O(N) as well, due to the additional space needed for the stack and the hashmap.