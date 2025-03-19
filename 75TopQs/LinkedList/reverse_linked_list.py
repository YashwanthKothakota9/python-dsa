# Given the head of a singly linked list and two positive integers left and right where left <= right, reverse all the nodes from the left to the right position, and return the updated list.

# Example 1:

# Input: [7, 8, 9, 10, 11], left = 2, right = 4
# Expected Output: [7, 10, 9, 8, 11]
# Justification: The nodes from position 2 to 4 (8, 9, 10) are reversed to become 10, 9, 8.
# Example 2:

# Input: [1, 2, 3, 4, 5, 6], left = 2, right = 5
# Expected Output: [1, 5, 4, 3, 2, 6]
# Justification: The nodes from position 2 to 5 (2, 3, 4, 5) are reversed to become 5, 4, 3, 2.
# Example 3:

# Input: [5, 6, 7, 8, 9], left = 1, right = 3
# Expected Output: [7, 6, 5, 8, 9]
# Justification: The nodes from position 1 to 3 (5, 6, 7) are reversed to become 7, 6, 5.

# To solve this problem, we will use a two-pointer technique along with a dummy node to simplify edge cases. The approach involves moving two pointers to the positions just before and at the start of the sublist that needs to be reversed. We'll then reverse the sublist in-place by adjusting the pointers.

# This approach is effective because it allows us to reverse the specific portion of the list without needing extra space for another list, keeping the space complexity low. By adjusting pointers directly, we ensure that the solution is efficient and runs in linear time relative to the length of the list.

# Step-by-Step Algorithm
# Initialize a dummy node:

# Create a dummy node with value 0 and set its next pointer to the head of the list. This helps to handle edge cases smoothly.
# Initialize a pointer prev to point to the dummy node.
# Move prev to the node just before the start of the sublist to be reversed:

# Iterate left - 1 times to move prev to the node right before the position left.
# Initialize pointers for reversing the sublist:

# Set a pointer start to prev.next, which points to the first node in the sublist to be reversed.
# Set a pointer then to start.next, which points to the node after start.
# Reverse the sublist from position left to right:

# Perform the reversal right - left times:
# Set start.next to then.next.
# Set then.next to prev.next.
# Set prev.next to then.
# Move then to start.next.
# Return the new head of the list:

# Return dummy.next, which points to the new head of the list after reversal.

# Complexity Analysis
# Time Complexity: O(n)
# We traverse the linked list a few times: once to reach the position before the sublist to be reversed, and then to reverse the sublist. This results in O(n) complexity, where n is the number of nodes in the list.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space regardless of the input size. We only use a few pointers for reversing the sublist.


class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class Solution:
    def reverse_between(self, head: Node, left: int, right: int) -> Node:
        if not head:
            return None

        dummy = Node(0)
        dummy.next = head
        prev = dummy

        for i in range(left-1):
            prev = prev.next  # type: ignore

        start = prev.next  # type: ignore
        then = start.next  # type: ignore

        for i in range(right-left):
            start.next = then.next  # type: ignore
            then.next = prev.next  # type: ignore
            prev.next = then  # type: ignore
            then = start.next  # type: ignore

        return dummy.next


def printList(head):
    while head:
        print(head.value, end="=>")
        head = head.next
    print()


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head1 = Node(7)
    head1.next = Node(8)
    head1.next.next = Node(9)
    head1.next.next.next = Node(10)
    head1.next.next.next.next = Node(11)
    result1 = solution.reverse_between(head1, 2, 4)
    printList(result1)  # Expected output: [7, 10, 9, 8, 11]

    # Example 2
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    head2.next.next.next = Node(4)
    head2.next.next.next.next = Node(5)
    head2.next.next.next.next.next = Node(6)
    result2 = solution.reverse_between(head2, 2, 5)
    printList(result2)  # Expected output: [1, 5, 4, 3, 2, 6]

    # Example 3
    head3 = Node(5)
    head3.next = Node(6)
    head3.next.next = Node(7)
    head3.next.next.next = Node(8)
    head3.next.next.next.next = Node(9)
    result3 = solution.reverse_between(head3, 1, 3)
    printList(result3)  # Expected output: [7, 6, 5, 8, 9]
