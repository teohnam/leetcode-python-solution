"""
Two Pointers

If nums[fast_pointer] != val:
- Copy nums[fast_pointer] to nums[slow_pointer].
- Increment slow_pointer.

Complexity:
- Time: O(n)
- Space: O(1)
"""
class Solution(object):
    def removeElement(self, nums, val):
        fast_pointer = 0    
        slow_pointer = 0

        while fast_pointer < len(nums):
            if nums[fast_pointer] != val:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
            fast_pointer += 1

        return slow_pointer

"""
Original Solution
- Time: O(n²) 
- Space: O(1)
"""
class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)- 1, -1, -1):
            if nums[i] == val:
                del nums[i]    

        return len(nums)