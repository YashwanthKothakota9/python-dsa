from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Stack(Generic[T]):
    class Node:
        def __init__(self, data: T) -> None:
            self.data: T = data  # type: ignore # Store the data in this node
            self.next: Optional['Stack.Node'] = None  # Initialize the next node as None

    def __init__(self) -> None:
        self.top: Optional[Stack.Node] = None  # Initialize the top of the stack as None

    def pop(self) -> T:
        if self.top is None:
            raise IndexError("pop from empty stack")  # Raise exception if the stack is empty
        item: T = self.top.data  # Store the top item's data
        self.top = self.top.next  # Update the top to be the next node
        return item  # Return the popped item

    def push(self, item: T) -> None:
        t: Stack.Node = self.Node(item)  # Create a new node with the provided data
        t.next = self.top  # Set the next of this new node to be the current top
        self.top = t  # Update the top to be the new node

    def peek(self) -> T:
        if self.top is None:
            raise IndexError("peek from empty stack")  # Raise exception if the stack is empty
        return self.top.data  # Return the top item's data

    def is_empty(self) -> bool:
        return self.top is None  # Return True if the stack is empty, False otherwise