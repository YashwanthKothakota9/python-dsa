class DlNode:
    def __init__(self,val = 0):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def isPalindrome(self,head):
        if not head or not head.next:
            return True
        tail = head
        while tail.next:
            tail = tail.next
        start = head
        end = tail
        # print(start.val," ",end.val)
        while start!=end and start.prev!=end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.prev
        return True

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    head1 = DlNode(1)
    head1.next = DlNode(2) # type: ignore
    head1.next.prev = head1 # type: ignore
    head1.next.next = DlNode(1) # type: ignore
    head1.next.next.prev = head1.next # type: ignore
    print(solution.isPalindrome(head1))  # Expected: True
