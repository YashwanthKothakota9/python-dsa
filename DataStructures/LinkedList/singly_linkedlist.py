class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert a new node at the beginning of the list
    def insert(self,val):
        new_node = Node(val)
        new_node.next = self.head # type: ignore
        self.head = new_node
    
    # Function to insert a new node after a given node
    def insert_after(self,prev_node,val):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete(self,key):
        temp = self.head
        if temp is not None:
            if temp.val == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.val == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
    
    def search(self,key):
        current = self.head
        while current != None:
            if current.val == key:
                return True
            current = current.next
        return False
    
if __name__=="__main__":
    llist = LinkedList()  # Create an empty list

    # Insert nodes into the list
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)

    # Search for a key in the list
    print("Search 2:", llist.search(2))  # True

    # Delete a node from the list by key
    llist.delete(2)

    # Check if the key is still present in the list
    print("Search 2:", llist.search(2))  # False
