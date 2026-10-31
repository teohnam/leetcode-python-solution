"""
Floyd's Cycle Detection Algorithm
Use fast and slow pointers:
- Fast pointer moves 2 steps at a time.
- Slow pointer moves 1 step at a time.

If the linked list has a cycle, the two pointers will eventually meet.
If fast pointer or fast.next is None, there is no cycle.
"""
class Solution(object):
    def hasCycle(self, head):
        fast_pointer = head
        slow_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                return True

        return False

            
                
        