# Tc: O(N) Sc: O(1)

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next
   
class Solution:
    def findCycleStart(self, head):
        cycle_length = 0
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle_length = self.calculate_cycle_length(slow)
                break
        return self.find_start_cycle(head, cycle_length)
    
    def calculate_cycle_length(self, slow):
        curr = slow
        cycle_length = 0
        while True:
            curr = curr.next
            cycle_length += 1
            if curr == slow:
                break
        return cycle_length
    
    def find_start_cycle(self, head, cycle_length):
        pointer1 = head
        pointer2 = head
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1
        
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return pointer1

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  # Create a cycle by connecting nodes
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

  # Create a different cycle
  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

  # Create a cycle that points back to the head
  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

main()
