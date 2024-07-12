# Given a head of the linked list, return the list after sorting it in ascending order.

# Examples
# Example 1:

# Input: [3, 1, 2]
# Expected Output: [1, 2, 3]
# Justification: The list is sorted in ascending order, with 1 coming before 2, and 2 before 3.
# Example 2:

# Input: [4]
# Expected Output: [4]
# Justification: A list with a single element is already sorted.
# Example 3:

# Input: [9, 8, 7, 6, 5, 4, 3, 2, 1]
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Justification: The list is sorted in ascending order, with each element being smaller than the next.

# To sort a linked list, a merge sort algorithm can be used, which is renowned for its efficiency with linked lists due to its recursive nature and the ability to sort lists without additional space requirements for arrays. The approach involves dividing the list into smaller sublists until each sublist contains a single element or is empty. This division is based on the principle of recursion, where the list is split into halves repeatedly.

# Once we have these small sublists, the next step is to merge them back together in a sorted manner. During the merging process, we compare the elements of the sublists and arrange them in ascending order. This merging is done until we reconstruct the entire list, but now in a sorted order.

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self,head):
        if not head or not head.next:
            return head
        
        slow,fast,prev = head, head, None
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None # type: ignore
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge(l1, l2)
    
    def merge(self,l1,l2):
        dummy = tail = Node(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next
    
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("null")
    
if __name__ == "__main__":
    solution = Solution()

    values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value) # type: ignore
        current = current.next # type: ignore

    print("Original List:")
    printList(head)

    head = solution.sortList(head)

    print("Sorted List:")
    printList(head)

# Tc: O(nlogn) Sc: O(logn)