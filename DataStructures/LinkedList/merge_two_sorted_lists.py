class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,l1,l2):
        dummy = Node(-1)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        return dummy.next
    
if __name__ == "__main__":
    solution = Solution()

    # Create the first example Node instances
    list1 = Node(1, Node(2, Node(3)))
    list2 = Node(1, Node(4))

    # Call mergeTwoLists method and print the result
    result = solution.mergeTwoLists(list1, list2)
    while result:
        print(result.val, end=" ")
        result = result.next
