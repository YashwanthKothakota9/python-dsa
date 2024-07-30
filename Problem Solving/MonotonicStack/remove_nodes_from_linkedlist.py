# Given the head node of a singly linked list, modify the list such that any node that has a node with a greater value to its right gets removed. The function should return the head of the modified list.

# Examples:

# Input: 5 -> 3 -> 7 -> 4 -> 2 -> 1
# Output: 7 -> 4 -> 2 -> 1
# Explanation: 5 and 3 are removed as they have nodes with larger values to their right.

# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5
# Explanation: 1, 2, 3, and 4 are removed as they have nodes with larger values to their right.

# Input: 5 -> 4 -> 3 -> 2 -> 1
# Output: 5 -> 4 -> 3 -> 2 -> 1
# Explanation: None of the nodes are removed as none of them have nodes with larger values to their right.

# We can use the monotonic stack strategy to keep track of the highest-valued nodes in the linked list, ensuring that any node with a higher value to its right gets removed.

# Starting from the head of the list, we will traverse each node. At each node, we will check the value of the node against the node at the top of the stack. If the current node has a higher value, we will pop the top value from the stack. We will keep repeating this until we encounter a node with a higher value or the stack is empty. Then, the current node is pushed onto the stack. This process ensures that the stack only contains nodes in decreasing order from bottom to top.


class Node:
    def __init__(self, value, next=None) -> None:
        self.val = value
        self.next = next

class Solution:
    def removeNodes(self, head):
        stack = []
        cur = head
        while cur:
            print(f"Stack: {stack}")
            while stack and stack[-1].val < cur.val:
                stack.pop()
            if stack:
                stack[-1].next = cur
            stack.append(cur)
            cur = cur.next
        return stack[0] if stack else None

solution = Solution()

# Creating the linked list 5 -> 3 -> 7 -> 4 -> 2 -> 1
head1 = Node(5)
head1.next = Node(3)
head1.next.next = Node(7)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(2)
head1.next.next.next.next.next = Node(1)
head1 = solution.removeNodes(head1)

# Printing the modified list: 7 -> 4 -> 2 -> 1
node = head1
while node:
    print(node.val, end=" -> " if node.next else "\n")
    node = node.next


# The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list. This is because every node is visited once while traversing the list. The inner loop may seem to increase the time complexity, but in fact, it doesn't, because each node is pushed and popped from the stack at most once, so the total operations are still proportional to n.

# The space complexity is also O(n). This is due to the extra space required for the stack. In the worst-case scenario (when the list is sorted in ascending order), all the nodes will be pushed onto the stack, requiring n space.

# Therefore, we say the algorithm is linear in both time and space complexity.