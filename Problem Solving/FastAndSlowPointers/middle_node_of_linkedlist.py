# # Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# # If the total number of nodes in the LinkedList is even, return the second middle node.

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# Example 3:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

# Tc: O(N) Sc: O(1)

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next
   
def MiddleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  # Print the middle node's value
  print("Middle Node: " + str(MiddleNode(head).val)) # type: ignore

  head.next.next.next.next.next = Node(6)
  # Print the middle node's value after adding a new node
  print("Middle Node: " + str(MiddleNode(head).val)) # type: ignore

  head.next.next.next.next.next.next = Node(7)
  # Print the middle node's value after adding another new node
  print("Middle Node: " + str(MiddleNode(head).val)) # type: ignore

# Call the main function to execute the code
main()
