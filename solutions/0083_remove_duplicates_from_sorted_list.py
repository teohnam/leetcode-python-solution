"""
Remove the next node if it has the same value as the current node; otherwise, move to the next node.
"""
class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head

        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        
        return head