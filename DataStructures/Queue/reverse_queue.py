class Solution:
    def reverse_queue(self,queue):
        stack=[]
        while queue:
            stack.append(queue.pop(0))
        while stack:
            queue.append(stack.pop())
        return queue

sol = Solution()
# Initialize a queue with some elements.
q = [1, 2, 3, 4, 5]

# Call the function to reverse the order of elements in the queue.
sol.reverse_queue(q)

# Print each element of the now-reversed queue.
for elem in q:
    print(elem, end=' ')