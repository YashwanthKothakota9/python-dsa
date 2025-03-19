# Given the head of a linked list, reverse each k node of the list at a time and return the modified list.

# Here, k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k, the remaining nodes at the end should stay as they are.

# Note: You can only change the nodes themselves, not the values inside them.

# Examples
# Example 1:

# Input: head = [1, 2, 3, 4, 5, 6], k = 3
# Expected Output: [3, 2, 1, 6, 5, 4]
# Justification: The list is reversed in groups of three. First group [1, 2, 3] becomes [3, 2, 1] and the second group [4, 5, 6] becomes [6, 5, 4].
# Example 2:

# Input: head = [1, 2, 3, 4, 5], k = 2
# Expected Output: [2, 1, 4, 3, 5]
# Justification: The list is reversed in groups of two. First group [1, 2] becomes [2, 1] and the second group [3, 4] becomes [4, 3]. The last node [5] remains unchanged.
# Example 3:

# Input: head = [1, 2, 3, 4, 5, 6, 7], k = 4
# Expected Output: [4, 3, 2, 1, 5, 6, 7]
# Justification: The list is reversed in groups of four. First group [1, 2, 3, 4] becomes [4, 3, 2, 1]. The remaining nodes [5, 6, 7] are left as they are because their count is less than k.

# Solution
# To solve this problem, we will traverse the linked list and reverse every k nodes. We need to handle the reversal in-place, ensuring we only modify the pointers of the nodes. We must also manage the situation where the number of nodes remaining at the end of the list is less than k, in which case those nodes should not be reversed. This approach is effective because it ensures that the nodes are only traversed once, giving an O(n) time complexity, where n is the number of nodes in the list.

# We will use a loop to process each group of k nodes. For each group, we will reverse the nodes by adjusting the pointers. After reversing each group, we will reconnect it to the previous part of the list. This method ensures that the nodes are reversed in place and the list remains properly connected.


# Algorithm Walkthrough
# Let's walkthrough the algorithm for head = [1, 2, 3, 4, 5, 6], k = 3

# Initialization:

# Create a dummy node: dummy = ListNode(0), dummy.next = head
# Initialize pointers: groupPrev = dummy, groupNext = dummy
# First Iteration:

# Move groupNext pointer k nodes ahead:
# Move to groupNext = groupNext.next (1)
# Move to groupNext = groupNext.next (2)
# Move to groupNext = groupNext.next (3)
# Check if there are k nodes:
# groupNext is not null, so continue.
# Reverse the first k nodes:

# Set initial pointers: prev = groupPrev.next (1), curr = prev.next (2)
# Reversal process:
# Step 1:
# prev.next = curr.next (1 -> 3)
# curr.next = groupPrev.next (2 -> 1)
# groupPrev.next = curr (dummy -> 2)
# curr = prev.next (3)
# List state: dummy -> 2 -> 1 -> 3 -> 4 -> 5 -> 6
# Step 2:
# prev.next = curr.next (1 -> 4)
# curr.next = groupPrev.next (3 -> 2)
# groupPrev.next = curr (dummy -> 3)
# curr = prev.next (4)
# List state: dummy -> 3 -> 2 -> 1 -> 4 -> 5 -> 6
# Move groupPrev pointer k nodes ahead: groupPrev = prev (1)
# Second Iteration:

# Move groupNext pointer k nodes ahead:
# Move to groupNext = groupNext.next (4)
# Move to groupNext = groupNext.next (5)
# Move to groupNext = groupNext.next (6)
# Check if there are k nodes:
# groupNext is not null, so continue.
# Reverse the second k nodes:

# Set initial pointers: prev = groupPrev.next (4), curr = prev.next (5)
# Reversal process:
# Step 1:
# prev.next = curr.next (4 -> 6)
# curr.next = groupPrev.next (5 -> 4)
# groupPrev.next = curr (1 -> 5)
# curr = prev.next (6)
# List state: dummy -> 3 -> 2 -> 1 -> 5 -> 4 -> 6
# Step 2:
# prev.next = curr.next (4 -> null)
# curr.next = groupPrev.next (6 -> 5)
# groupPrev.next = curr (1 -> 6)
# curr = prev.next (null)
# List state: dummy -> 3 -> 2 -> 1 -> 6 -> 5 -> 4
# Move groupPrev pointer k nodes ahead: groupPrev = prev (4)
# End of list:

# The loop ends as there are no more nodes to process.
# Return the new head:

# Return dummy.next which points to the new head of the reversed list: 3 -> 2 -> 1 -> 6 -> 5 -> 4


# Complexity Analysis
# Time Complexity: The algorithm traverses each node in the list a constant number of times. Therefore, the time complexity is O(n), where (n) is the number of nodes in the list.
# Space Complexity: The algorithm uses a constant amount of extra space regardless of the input size. Therefore, the space complexity is O(1).


class Node:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def reverse_k_group(self, head, k):
        dummy = Node(0)
        dummy.next = head

        group_prev = dummy
        group_next = dummy

        while True:
            count = 0
            while count < k and group_next is not None:
                group_next = group_next.next
                count += 1
            if group_next is None:
                break

            prev = group_prev.next  # type:ignore
            curr = prev.next  # type:ignore

            for i in range(1, k):
                prev.next = curr.next  # type:ignore
                curr.next = group_prev.next  # type:ignore
                group_prev.next = curr  # type:ignore
                curr = prev.next  # type:ignore

            group_prev = prev
            group_next = prev

        return dummy.next


def print_list(head):
    while head is not None:
        print(head.val, end="->")
        head = head.next
    print(None)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    head1 = Node(1)
    head1.next = Node(2)  # type: ignore
    head1.next.next = Node(3)  # type: ignore
    head1.next.next.next = Node(4)  # type: ignore
    head1.next.next.next.next = Node(5)  # type: ignore
    head1.next.next.next.next.next = Node(6)  # type: ignore
    result1 = sol.reverse_k_group(head1, 3)  # type: ignore
    print_list(result1)

    # Example 2
    head2 = Node(1)
    head2.next = Node(2)  # type: ignore
    head2.next.next = Node(3)  # type: ignore
    head2.next.next.next = Node(4)  # type: ignore
    head2.next.next.next.next = Node(5)  # type: ignore
    result2 = sol.reverse_k_group(head2, 2)  # type: ignore
    print_list(result2)
