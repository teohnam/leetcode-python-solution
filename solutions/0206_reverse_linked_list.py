"""
Recursive approach
"""
class Solution(object):
    def reverseList(self, head):
        # Base case: the list is empty or has only one node.
        if head is None or head.next is None:
            return head

        # Reverse the rest of the list and save its new head.
        new_head = self.reverseList(head.next)

        # Reverse the link between the current node and the next node.
        head.next.next = head
        head.next = None

        # Return the new head of the reversed list.
        return new_head

"""
Iterative approach
"""
class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None

        while curr is not None:
            # Save the next node before reversing the link.
            next_node = curr.next

            # Reverse the current node's link.
            curr.next = prev

            # Advance both pointers.
            prev = curr
            curr = next_node

        # Return the new head of the reversed list.
        return prev