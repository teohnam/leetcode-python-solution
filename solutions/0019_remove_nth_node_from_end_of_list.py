# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        def recursive(node):
            if node is None:
                return 0 

            # Record the position of the current node
            count = recursive(node.next) + 1

            # Calculate the current node's position from the end
            if count == n + 1:
                node.next = node.next.next

            return count

        # Introduce a dummy node to handle the situation when the node is removed
        dummy = ListNode(0)
        dummy.next = head

        recursive(dummy)
        return dummy.next
   