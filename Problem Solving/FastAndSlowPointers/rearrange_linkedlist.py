# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should use only constant space the input LinkedList should be modified in-place.

# Tc: O(N) Sc: O(1)

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
  def reorder(self, head):
    if head is None or head.next is None:
      return head

    # find middle of the LinkedList
    slow, fast = head, head
    while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next

    # slow is now pointing to the middle node
    head_second_half = self.reverse(slow)  # reverse the second half
    head_first_half = head

    # rearrange to produce the LinkedList in the required order
    while head_first_half is not None and head_second_half is not None:
      temp = head_first_half.next
      head_first_half.next = head_second_half
      head_first_half = temp

      temp = head_second_half.next
      head_second_half.next = head_first_half
      head_second_half = temp

    # set the next of the last node to 'None'
    if head_first_half is not None:
      head_first_half.next = None
    return head


  def reverse(self, head):
    prev = None
    while head is not None:
      next = head.next
      head.next = prev
      prev = head
      head = next
    return prev

  def print_list(self, head):
    temp = head
    while temp is not None:
      print(str(temp.val) + " ", end='')
      temp = temp.next
    print()


def main():
  sol = Solution()
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  sol.reorder(head)
  sol.print_list(head)


main()
