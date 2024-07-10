class Stack:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.top = None
    
    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        item = self.top.data
        self.top = self.top.next
        return item
    
    def push(self,item):
        t = self.Node(item)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    