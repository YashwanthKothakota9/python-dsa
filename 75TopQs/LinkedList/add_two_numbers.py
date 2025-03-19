# You are given two non-empty linked lists that represent two non-negative integers, where each node contains the single digit. The digits are stored in reverse order. Add these two numbers and return the sum as a linked list.

# You can assume the numbers do not have leading zeros, except for the number 0 itself.

# Examples
# Example 1:

# Input: l1: [1, 2, 3], l2: [4, 5, 6]
# Expected Output: [5, 7, 9]
# Justification: 321 + 654 = 975, which in reverse order is [5, 7, 9].
# Example 2:

# Input: l1: [7, 8], l2: [6, 7, 8, 9]
# Expected Output: [3, 6, 9, 9]
# Justification: 87 + 9876 = 9963, which in reverse order is [3, 6, 9, 9].
# Example 3:

# Input: l1: [0], l2: [0]
# Expected Output: [0]
# Justification: 0 + 0 = 0, which in reverse order is [0].


# To solve this problem, we will iterate through both linked lists while adding corresponding digits along with any carry from the previous addition. We'll start from the least significant digit (head of the list). If the sum of the digits and carry is 10 or more, we'll set the current node value to the remainder when divided by 10 and carry forward the quotient. This approach ensures that we handle all digit additions and carries correctly as we move through the lists.

# This approach works well because it mimics the manual addition process, dealing with each digit and carrying over values as needed. It efficiently handles linked lists of different lengths by continuing to process the longer list once the shorter one is exhausted, ensuring that all digits are accounted for in the final sum.

# Complexity Analysis
# Time Complexity: O(max(m,n)), where m and n are the lengths of the two input linked lists. We iterate through both lists once.
# Space Complexity: O(max(m,n)). We create a new linked list that holds the sum of the input linked lists, which could be as long as the longer input list plus one extra node for a possible carry.


class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Node, l2: Node) -> Node:
        dummy = Node(0)
        current = dummy
        carry = 0

        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.value
                l1 = l1.next  # type: ignore
            if l2:
                sum += l2.value
                l2 = l2.next  # type: ignore
            carry = sum // 10
            current.next = Node(sum % 10)
            current = current.next
        # If carry is still greater than 0, add a new node with carry value
        if carry > 0:
            current.next = Node(carry)

        return dummy.next  # Return the result list


def print_list(node: Node):
    while node:
        print(node.value, end='=>')
        node = node.next  # type: ignore
    print()


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(3)

    l2 = Node(4)
    l2.next = Node(5)
    l2.next.next = Node(6)

    result = solution.add_two_numbers(l1, l2)
    print_list(result)  # Expected output: 5 7 9

    # Example 2
    l1 = Node(7)
    l1.next = Node(8)

    l2 = Node(6)
    l2.next = Node(7)
    l2.next.next = Node(8)
    l2.next.next.next = Node(9)

    result = solution.add_two_numbers(l1, l2)
    print_list(result)  # Expected output: 3 6 9 9

    # Example 3
    l1 = Node(0)
    l2 = Node(0)

    result = solution.add_two_numbers(l1, l2)
    print_list(result)  # Expected output: 0
