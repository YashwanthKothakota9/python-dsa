# Given an array, print the Next Greater Element (NGE) for every element.

# The Next Greater Element for an element x is the first greater element on the right side of x in the array.

# Elements for which no greater element exist, consider the next greater element as -1.

# Examples
# Example 1:

#  Input: [4, 5, 2, 25]
#  Output: [5, 25, 25, -1]
#  Explanation: The NGE for 4 is 5, 5 is 25, 2 is 25, and there is no NGE for 25.
# Example 1:

#  Input: [13, 7, 6, 12]
#  Output: [-1, 12, 12, -1]

class Solution:
    def nextGreaterElement(self, arr):
        s = []
        res = [-1] * len(arr)
        
        for i in range(len(arr)-1,-1,-1):
            while s and s[-1] <= arr[i]:
                s.pop()
            if s:
                res[i] = s[-1]
            s.append(arr[i])
        
        return res

sol = Solution()
print(sol.nextGreaterElement([4, 5, 2, 25]))  # Example usage
print(sol.nextGreaterElement([13, 7, 6, 12]))  # Example usage
print(sol.nextGreaterElement([1, 2, 3, 4, 5]))  # Example usage


# Time Complexity: The worst-case time complexity of this algorithm is O(n) as every element is pushed and popped from the stack exactly once.

# Space Complexity: The space complexity of this algorithm is O(n) as we are using a stack and an array to store the next greater elements.