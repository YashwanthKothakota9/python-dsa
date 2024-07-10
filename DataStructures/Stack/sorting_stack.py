# Given a stack, sort it using only stack operations (push and pop).

# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The values in the stack are to be sorted in descending order, with the largest elements on top.

# 1. Input: [34, 3, 31, 98, 92, 23]
#    Output: [3, 23, 31, 34, 92, 98]

# 2. Input: [4, 3, 2, 10, 12, 1, 5, 6]
#    Output: [1, 2, 3, 4, 5, 6, 10, 12]

# 3. Input: [20, 10, -5, -1]
#    Output: [-5, -1, 10, 20]


# Tc: O(n*n) Sc: O(n)
class Solution:
    def sortStack(self,stack):
        # Create an empty stack to store the sorted elements
        tempStack = []
        # Continue sorting until the original stack is empty
        while stack:
            # Pop the top element from the original stack
            temp = stack.pop()
            # Move elements from the temporary stack back to the original stack
            # until we find the correct position for the current element
            while tempStack and tempStack[-1] > temp:
                stack.append(tempStack.pop())
            # Place the current element in its correct sorted position in the temporary stack
            tempStack.append(temp)
        return tempStack
    
def main():
    sol = Solution();
    stack = [34, 3, 31, 98, 92, 23]
    print("Input: ", stack)
    print("Sorted Output: ", sol.sortStack(stack))

if __name__ == '__main__':
    main()