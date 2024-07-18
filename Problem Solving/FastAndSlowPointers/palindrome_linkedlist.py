# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true

# Example 2:
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false

# We can use the Fast & Slow pointers method similar to Middle of the LinkedList to find the middle node of the LinkedList.
# Once we have the middle of the LinkedList, we will reverse the second half.
# Then, we will compare the first half with the reversed second half to see if the LinkedList represents a palindrome.
# Finally, we will reverse the second half of the LinkedList again to revert and bring the LinkedList back to its original form.


# Tc: O(N) Sc: O(1)


from typing import Optional


class Node:
    def __init__(self, value, next: Optional['Node']=None):
        self.val = value
        self.next = next

class Solution:
    def isPalindrome(self, head:Optional[Node]) -> bool:
        if head is None or head.next is None:
            return True
        
        slow:Optional[Node] = head
        fast:Optional[Node] = head
        while fast is not None and fast.next is not None:
            slow = slow.next # type: ignore
            fast = fast.next.next
        
        head_second_half = self.reverse(slow)
        copy_head_second_half = head_second_half
        
        while head is not None and head_second_half is not None:
            if head.val != head_second_half.val:
                break
            head = head.next
            head_second_half = head_second_half.next
        
        self.reverse(copy_head_second_half)
        
        if head is None or head_second_half is None:
            return True
        
        return False
        
    
    def reverse(self, head: Optional[Node]) -> Optional[Node]:
        prev = None
        while head is not None:
            next = head.next
            head.next = prev 
            prev = head
            head = next
        return prev
    
def main() -> None:
  sol = Solution()
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(sol.isPalindrome(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(sol.isPalindrome(head)))


main()
