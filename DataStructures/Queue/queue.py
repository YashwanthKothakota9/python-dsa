class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None
        self.size = 0
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    
if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display front element
    print("Front element:", queue.peek())
    # Dequeue and display the dequeued element
    print("Dequeued:", queue.dequeue())
    # Display front element again
    print("Front element:", queue.peek())
    # Display the size of the queue
    print("Queue size:", queue.get_size())
