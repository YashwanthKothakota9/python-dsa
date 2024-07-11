class DLNode:
    def __init__(self,val = None) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        new_node = DLNode(val)
        new_node.next = self.head # type: ignore
        if self.head is not None:
            self.head.prev = new_node # type: ignore
        self.head = new_node
    
    def insert_after(self, prev_node, val):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")  # Check if the previous node exists
            return
        new_node = DLNode(val)  # Create a new node with the given value
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def delete(self,key):
        temp = self.head
        while temp is not None:
            if temp.val == key:
                # If the node with the specified key is found, remove it from the list
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
    
    def search(self, key):
        current = self.head
        while current is not None:
            if current.val == key:
                return True  # Return True if the key is found in the list
            current = current.next
        return False  # Return False if the key is not found in the list

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3) 
    print("Search 2:", dll.search(2))  # True
    dll.delete(2)
    print("Search 2:", dll.search(2))  # False

