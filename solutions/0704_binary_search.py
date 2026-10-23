
"""
Optimized solution: O(log n) time complexity

Use left and right boundaries to track the search range
in the original list instead of creating new lists through slicing.
"""
class Solution(object):
    def search(self, nums, target):
        def binary_search(left, right):
            if left > right:
                return -1

            # Target the search range
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            return binary_search(left, mid - 1)

        return binary_search(0, len(nums) - 1)


"""
Original solution: O(n) time complexity in the worst case

Uses list slicing at each recursive call, which creates new lists
and adds overhead.
"""
class Solution(object):
    def search(self, nums, target):
        if len(nums) <= 0:
            return -1

        mid = len(nums) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            result = self.search(nums[mid+1:], target)
            if result == -1:
                return -1
            return result + mid + 1
        if target < nums[mid]:
            return self.search(nums[:mid], target)
