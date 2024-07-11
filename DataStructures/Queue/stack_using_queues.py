from queue import Queue

class Solution:
    def __init__(self):
        # Initialize two Queues, 'main' and 'aux' for stack implementation
        self.main = Queue()
        self.aux = Queue()

    def push(self, val):
        # Push the value into 'aux' Queue
        self.aux.put(val)
        # Move all elements from 'main' to 'aux', effectively reversing the order
        while not self.main.empty():
            self.aux.put(self.main.get())
        # Swap 'main' and 'aux' Queues to maintain the correct stack order
        self.main, self.aux = self.aux, self.main

    def pop(self):
        # Pop and return the top element from 'main' Queue, which simulates popping from the stack
        return self.main.get()

# Testing
stack = Solution()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3 (last pushed element)
print(stack.pop())  # Should print 2 (element pushed before 3)
