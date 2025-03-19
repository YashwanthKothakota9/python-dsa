# Given the head of a singly linked list, rearrange the nodes such that all nodes with odd indices are grouped together followed by all nodes with even indices, and return the updated list

# The order of the nodes within the odd and even groups should remain as in the original list.

# The reordering should be done in-place with  extra space and  time complexity.

# Examples
# Example 1:

# Input: head = [10, 20, 30, 40, 50, 60]
# Expected Output: [10, 30, 50, 20, 40, 60]
# Justification: Nodes at indices 1, 3, and 5 are grouped together first (10, 30, 50), followed by nodes at indices 2, 4, and 6 (20, 40, 60).
# Example 2:

# Input: head = [1, 3, 5, 7, 9]
# Expected Output: [1, 5, 9, 3, 7]
# Justification: Nodes at indices 1, 3, and 5 are grouped together first (1, 5, 9), followed by nodes at indices 2 and 4 (3, 7).
# Example 3:

# Input: head = [2, 4, 6, 8, 10, 12, 14]
# Expected Output: [2, 6, 10, 14, 4, 8, 12]
# Justification: Nodes at indices 1, 3, 5, and 7 are grouped together first (2, 6, 10, 14), followed by nodes at indices 2, 4, and 6 (4, 8, 12).

# Solution
# To solve this problem, we need to rearrange the linked list nodes so that nodes at odd indices come before nodes at even indices. We'll maintain two pointers: one for the odd-indexed nodes and one for the even-indexed nodes. By traversing the list once, we can link all odd-indexed nodes together, and then all even-indexed nodes. Finally, we'll link the last odd-indexed node to the first even-indexed node. This approach works efficiently because it only requires a single pass through the list and uses constant space.

# This method is effective because it leverages the existing structure of the linked list and avoids additional space allocation, making it suitable for large datasets.

# Time Complexity
# The algorithm traverses the linked list only once, where each node is visited and processed exactly once. Thus, the time complexity is O(n), where n is the number of nodes in the linked list.

# Space Complexity
# The algorithm rearranges the nodes in place without using any extra data structures that grow with the size of the input. Therefore, the space complexity is O(1).


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def odd_even_list(self, head):
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


def print_list(head):
    # Helper function to print the linked list
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")


head1 = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))
solution = Solution()
result1 = solution.odd_even_list(head1)
print_list(result1)  # Output: 10 -> 30 -> 50 -> 20 -> 40 -> 60 -> None

# Example 2
head2 = Node(1, Node(3, Node(5, Node(7, Node(9)))))
result2 = solution.odd_even_list(head2)
print_list(result2)  # Output: 1 -> 5 -> 9 -> 3 -> 7 -> None

# Example 3
head3 = Node(2, Node(4, Node(6, Node(8, Node(10)))))
result3 = solution.odd_even_list(head3)
print_list(result3)  # Output: 2 -> 6 -> 10 -> 4 -> 8 -> None
