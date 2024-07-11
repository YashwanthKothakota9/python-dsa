# Given a singly linked list, swap every two adjacent nodes and return the head of the modified list.

# If the total number of nodes in the list is odd, the last node remains in place. Every node in the linked list contains a single integer value.

# Input: [1, 2, 3, 4]
# Output: [2, 1, 4, 3]
# Justification: Pairs (1,2) and (3,4) are swapped.

# Input: [7, 8, 9, 10, 11]
# Output: [8, 7, 10, 9, 11]
# Justification: Pairs (7,8) and (9,10) are swapped. 11 remains in its place as it has no adjacent node to swap with.

# Input: [5, 6]
# Output: [6, 5]
# Justification: The pair (5,6) is swapped.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head:Node)->Node:

        # Initialize a dummy node to maintain the new head of the list after swapping.
        dummy = Node(0)
        dummy.next = head
        # Previous node to maintain the node previous to the current pair being swapped.
        prev = dummy

        # Continue swapping until no pairs are left.
        while head and head.next:
            # Initialize the first and second nodes of the pair to be swapped.
            first = head
            second = head.next

            # Adjust the pointers to perform the swap.
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair.
            head = first.next
            prev = first
        
        return dummy.next
    
if __name__ == "__main__":
    solution = Solution()
    
    # Initialize the list and perform the swap.
    head = Node(1, Node(2, Node(3, Node(4, Node(9)))))
    new_head = solution.swapPairs(head)
    # Print the list after swapping pairs.
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next