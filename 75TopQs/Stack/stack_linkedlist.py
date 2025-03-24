class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top  # type:ignore
        self.top = newNode
        print(f"{value} pushed to stack.")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! No elements to pop.")
            return -1
        popped_value = self.top.val  # type:ignore
        self.top = self.top.next  # type:ignore
        return popped_value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        return self.top.val  # type:ignore

    def isEmpty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Solution()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())  # Output: 30

    print("Popped:", stack.pop())  # Output: 30
    print("Popped:", stack.pop())  # Output: 20

    print("Is stack empty?", stack.isEmpty())  # Output: False
    stack.pop()  # Popping last element
    print("Is stack empty?", stack.isEmpty())  # Output: True
