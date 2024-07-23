# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

# The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in Reverse a LinkedList. Here are the steps we need to follow:

# Skip the first p-1 nodes, to reach the node at position p.
# Remember the node at position p-1 to be used later to connect with the reversed sub-list.
# Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
# Connect the p-1 and q+1 nodes to the reversed sub-list.

class Node:
    def __init__(self, value, next=None) -> None:
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head, p, q):
        if p == q:
            return head
        
        # after skipping 'p-1' nodes, current will point to 'p'th node
        curr, prev = head, None
        i = 0
        while curr is not None and i < p-1:
            prev = curr
            curr = curr.next
            i += 1
        
        # we are interested in three parts of the LinkedList, the part before index 'p',
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = prev
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = curr
        next = None
        
        i = 0
        # reverse nodes between 'p' and 'q'
        while curr is not None and i < q-p+1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        
        # connect with the first part
        if last_node_of_first_part is not None:
            # 'previous' is now the first node of the sub-list
            last_node_of_first_part.next = prev
        else:
            # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
            head = prev
        
        # connect with the last part
        last_node_of_sub_list.next = curr
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

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)

if __name__ == "__main__":
    main()
    

# --------------------------------------------------------------

# Problem 1: Reverse the first ‘k’ elements of a given LinkedList.

# Solution: This problem can be easily converted to our parent problem; to reverse the first ‘k’ nodes of the list, we need to pass p=1 and q=k.

# Problem 2: Given a LinkedList with ‘n’ nodes, reverse it based on its size in the following way:

# If ‘n’ is even, reverse the list in a group of n/2 nodes.
# If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
# Solution: When ‘n’ is even we can perform the following steps:

# Reverse first ‘n/2’ nodes: head = reverse(head, 1, n/2)
# Reverse last ‘n/2’ nodes: head = reverse(head, n/2 + 1, n)
# When ‘n’ is odd, our algorithm will look like:

# head = reverse(head, 1, n/2)
# head = reverse(head, n/2 + 2, n)
# Please note the function call in the second step. We’re skipping two elements as we will be skipping the middle element.