# Given the head of a LinkedList with a cycle, find the length of the cycle.

# Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to find the length of the cycle.

# Tc: O(N) Sc: O(1)

from typing import Optional


class Node:
    def __init__(self, value, next:Optional['Node'] = None) -> None:
        self.val = value
        self.next: Optional[Node] = next
    
class Solution:
    def findCycleLength(self, head:Optional[Node]) -> int:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next # type: ignore
            if slow == fast:
                return self.calculate_cycle_length(slow) # type: ignore
        return 0
    
    def calculate_cycle_length(self, slow: Node)->int:
        curr:Node = slow
        cycle_length = 0
        while True:
            curr = curr.next # type: ignore
            cycle_length += 1
            if curr == slow:
                break
        return cycle_length

def main() -> None:
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  
  # Create a cycle in the linked list
  head.next.next.next.next.next.next = head.next.next
  
  # Find and print the length of the cycle
  print("LinkedList cycle length: " + str(sol.findCycleLength(head)))

  # Create a longer cycle in the linked list
  head.next.next.next.next.next.next = head.next.next.next
  
  # Find and print the length of the longer cycle
  print("LinkedList cycle length: " + str(sol.findCycleLength(head)))

main()
