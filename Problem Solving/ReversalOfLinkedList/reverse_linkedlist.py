class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head):
        prev, curr, next = None, head, None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end = " -> ")
        temp = temp.next
    print("null")

def main():
    sol = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)

if __name__ == "__main__":
    main()

# Time Complexity
# The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.

# Space Complexity
# We only used constant space, therefore, the space complexity of our algorithm is O(1).