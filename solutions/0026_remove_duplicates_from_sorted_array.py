"""
Two Pointers

- If nums[fast_pointer] == nums[slow_pointer]:
    - Move fast_pointer forward.
- If nums[fast_pointer] != nums[slow_pointer]:
    - Increment slow_pointer.
    - Copy nums[fast_pointer] to nums[slow_pointer].

Complexity:
- Time: O(n)
- Space: O(1)
"""
class Solution(object):
    def removeDuplicates(self, nums):
        fast_pointer = 1
        slow_pointer = 0

        while fast_pointer < len(nums):  
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]
            fast_pointer += 1

        return slow_pointer + 1