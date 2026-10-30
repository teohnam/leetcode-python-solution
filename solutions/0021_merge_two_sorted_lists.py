"""
Approach: Iterative (Two Pointers)

1. Create a dummy `ListNode(0)` as the starting point of the merged list. Initialize `current_node` to point to the dummy node.
2. Compare the current nodes of `list1` and `list2`, and attach the smaller node to `current_node.next`.
3. Move the corresponding input list pointer forward, then move `current_node` forward.
4. Repeat until one of the input lists reaches `None`.
5. Attach the remaining nodes directly to `current_node.next`, since they are already sorted.
6. Return `merged_list.next` to exclude the dummy node.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged_list = ListNode(0)
        current_node = merged_list

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
                current_node = current_node.next
            else:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next

        current_node.next = list1 if list1 is not None else list2

        return merged_list.next
        
        