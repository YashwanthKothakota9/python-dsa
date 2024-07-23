# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.


# Another way of defining the rotation is to take the sub-list of ‘k’ ending nodes of the LinkedList and connect them to the beginning. Other than that we have to do three more things:

# Connect the last node of the LinkedList to the head, because the list will have a different tail after the rotation.
# The new head of the LinkedList will be the node at the beginning of the sublist.
# The node right before the start of sub-list will be the new tail of the rotated LinkedList.

# Time Complexity
# The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.

# Space Complexity
# We only used constant space, therefore, the space complexity of our algorithm is O(1).


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate(self, head, rotations):
        if head is None or head.next is None or rotations <= 0:
            return head
        
        # find the length and the last node of the list
        last_node = head
        list_length = 1
        while last_node.next is not None:
            last_node = last_node.next 
            list_length += 1
        
        # connect the last node with the head to make it a circular list
        last_node.next = head
        rotations %= list_length 
        skip_length = list_length - rotations
        last_node_of_rotated_list = head
        for i in range(skip_length - 1):
            last_node_of_rotated_list = last_node_of_rotated_list.next
        
        # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
        head = last_node_of_rotated_list.next
        last_node_of_rotated_list.next = None
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

  print("Nodes of original LinkedList are: ", end='')
  print_list(head)
  result = sol.rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  print_list(result)


main()
