# Given a stack, sort it using only stack operations (push and pop).

# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The values in the stack are to be sorted in descending order, with the largest elements on top.

# Examples
# 1. Input: [34, 3, 31, 98, 92, 23]
#    Output: [3, 23, 31, 34, 92, 98]

# 2. Input: [4, 3, 2, 10, 12, 1, 5, 6]
#    Output: [1, 2, 3, 4, 5, 6, 10, 12]

# 3. Input: [20, 10, -5, -1]
#    Output: [-5, -1, 10, 20]


class Solution:
    def sortStack(self, stack):
        tempStack = []
        while stack:
            temp = stack.pop()
            
            while tempStack and tempStack[-1] > temp:
                stack.append(tempStack.pop())
            
            tempStack.append(temp)
        return tempStack

sol = Solution()
stack = [34, 3, 31, 98, 92, 23]
print("Input: ", stack)
print("Sorted Output: ", sol.sortStack(stack))

# Time Complexity

# The time complexity of the sort stack algorithm is O(n^2), where n is the number of elements in the stack. This is because, in the worst case, for every element that we pop from the input stack, we might have to pop all the elements in the temporary stack (and push them back to the original stack) to find the correct place to insert the element. Since we have to do this for all n elements, the time complexity is n*n=n^2.

# Space Complexity

# The space complexity of the algorithm is O(n). This is because we use an additional temporary stack to sort the elements. In the worst-case scenario, this temporary stack could store all the elements of the original stack. Thus, the space complexity is directly proportional to the number of elements in the input stack, making it linear, O(n).

# Please note that the space complexity does not count the input size itself (the input stack in this case), it only counts the extra space we use related to the size of the input. If we were to count the input size as well, the total space used would be O(2n), but since we drop the constant factor when expressing space complexity, so it remains O(n).