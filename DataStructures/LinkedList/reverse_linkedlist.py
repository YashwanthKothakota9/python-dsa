class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    @staticmethod
    def printList(head):
        while head:
            print(head.val,end=" ")
            head = head.next
        print()
        
if __name__ == '__main__':
    sol = Solution()
    head1 = Node(3, Node(5, Node(2)))
    Solution.printList(sol.reverseList(head1))