# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.


# The problem follows the In-place Reversal of a LinkedList pattern and is quite similar to Reverse a Sub-list. The only difference is that we have to reverse all the sub-lists. We can use the same approach, starting with the first sub-list (i.e. p=1, q=k) and keep reversing all the sublists of size ‘k’.

# Time Complexity
# The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.

# Space Complexity
# We only used constant space, therefore, the space complexity of our algorithm is O(1).

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head, k):
        if k <= 1 or head is None:
            return head
        
        curr, prev = head, None
        while True:
            last_node_of_prev_part = prev
            last_node_of_sublist = curr
            next = None
            i=0
            while curr is not None and i < k:
                next = curr.next
                curr.next = prev
                prev=curr
                curr = next
                i += 1
            
            if last_node_of_prev_part is not None:
                last_node_of_prev_part.next = prev
            else:
                head = prev
            
            last_node_of_sublist.next = curr
            
            if curr is None:
                break
            prev = last_node_of_sublist
        return head


def print_list(head):
    temp = head
    while temp is not None:
      print(temp.val, end=" -> ")
      temp = temp.next
    print("null")

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  print_list(head)
  
  result = sol.reverse(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  print_list(result)


main()
