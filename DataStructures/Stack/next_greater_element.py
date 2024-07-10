# Given an array, print the Next Greater Element (NGE) for every element.

# The Next Greater Element for an element x is the first greater element on the right side of x in the array.

# Elements for which no greater element exist, consider the next greater element as -1.

# Input: [4, 5, 2, 25]
#  Output: [5, 25, 25, -1]

# Input: [13, 7, 6, 12]
#  Output: [-1, 12, 12, -1]

class Solution:
    def next_greater_element(self,arr):
        # Initialize an empty stack and a result list with -1 values
        stack = []
        res = [-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            # While the stack is not empty and the top element of the stack is less than or equal to the current element
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            # If the stack is not empty, set the result for the current element to the top element of the stack
            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])
        return res
    
def main():
    sol = Solution()
    print(sol.next_greater_element([4, 5, 2, 25]))  # Example usage
    print(sol.next_greater_element([13, 7, 6, 12]))  # Example usage
    print(sol.next_greater_element([1, 2, 3, 4, 5]))  # Example usage

if __name__ == '__main__':
    main()