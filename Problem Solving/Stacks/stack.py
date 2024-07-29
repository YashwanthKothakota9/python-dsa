class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.stack[-1]
