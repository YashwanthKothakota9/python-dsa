from typing import Optional

class Node:
    def __init__(self, val: int):
        self.val:int = val
        self.next: Optional[Node] = None

class Solution:
    def removeNodes(self, head: Optional[Node], target:int) -> Optional[Node]:
        if head is None:
            return None
        
        # Recursively remove nodes with target value from the remaining list
        head.next = self.removeNodes(head.next, target)
        
        # Check if the current node has the target value
        if head.val == target:
            # Skip the current node and return the modified list
            return head.next
        
        # Return the current node as the new head of the modified list
        return head

    def print_linked_list(self, head: Optional[Node]) -> None:
      current: Optional[Node] = head
      while current:
          print(current.val, end=" -> ")
          current = current.next
      print("null")


sol = Solution()
head1: Node = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(2)

print("Original Linked List 1: ", end="")
sol.print_linked_list(head1)

# Remove nodes with value 2 from linked list
modified_head1 = sol.removeNodes(head1, 2)
print("Modified Linked List 1: ", end="")
sol.print_linked_list(modified_head1)

# Example 2
head2: Node = Node(2)
head2.next = Node(2)
head2.next.next = Node(2)
head2.next.next.next = Node(2)
head2.next.next.next.next = Node(2)

print("Original Linked List 2: ", end="")
sol.print_linked_list(head2)

# Remove nodes with value 2 from linked list
modified_head2 = sol.removeNodes(head2, 2)
print("Modified Linked List 2: ", end="")
sol.print_linked_list(modified_head2)

# Example 3
head3: Node = Node(1)
head3.next = Node(3)
head3.next.next = Node(5)
head3.next.next.next = Node(7)

print("Original Linked List 3: ", end="")
sol.print_linked_list(head3)

# Remove nodes with value 2 from linked list
modified_head3 = sol.removeNodes(head3, 2)
print("Modified Linked List 3: ", end="")
sol.print_linked_list(modified_head3)          
