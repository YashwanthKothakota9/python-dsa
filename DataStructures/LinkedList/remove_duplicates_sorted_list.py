class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeDuplicates(self,head):
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
    def printList(self, head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("null")   

if __name__ == "__main__":
    solution = Solution()
    
    # Test Example 1
    head1 = Node(1, Node(1, Node(2)))
    solution.printList(head1)
    result1 = solution.removeDuplicates(head1) # Expected: 1 -> 2
    solution.printList(result1)
    
    # Test Example 2
    head2 = Node(1, Node(2, Node(2, Node(3))))
    solution.printList(head2)
    result2 = solution.removeDuplicates(head2) # Expected: 1 -> 2 -> 3
    solution.printList(result2)
    
    # Test Example 3
    head3 = Node(3, Node(3, Node(3)))
    solution.printList(head3)
    result3 = solution.removeDuplicates(head3) # Expected: 3
    solution.printList(result3)
