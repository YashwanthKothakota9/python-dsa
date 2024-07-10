class Stack:
    def __init__(self, size):
        # Initialize the stack with a specified size
        self.stack = [None] * size
        # Initialize the top pointer to -1, indicating an empty stack
        self.top = -1

    def push(self, data):
        # Check if the stack is full
        if self.top == len(self.stack) - 1:
            raise Exception('Stack is full')
        # Increment the top pointer
        self.top += 1
        # Add the data to the stack at the current top position
        self.stack[self.top] = data

    def pop(self):
        # Check if the stack is empty
        if self.isEmpty():
            raise Exception('Stack is empty')
        # Retrieve the data from the top of the stack
        data = self.stack[self.top]
        # Remove the data from the stack by setting it to None
        self.stack[self.top] = None
        # Decrement the top pointer
        self.top -= 1
        # Return the popped data
        return data

    def peek(self):
        # Check if the stack is empty
        if self.isEmpty():
            raise Exception('Stack is empty')
        # Return the data at the top of the stack without removing it
        return self.stack[self.top]

    def isEmpty(self):
        # Check if the stack is empty by examining the top pointer
        return self.top == -1
