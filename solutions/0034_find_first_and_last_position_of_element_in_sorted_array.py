"""
Time: O(log n)

Use two binary searches:
- Find the first occurrence by continuing to search the left half after finding the target.
- Find the last occurrence by continuing to search the right half after finding the target.

Each search halves the remaining search range.
"""
class Solution(object):
    def searchRange(self, nums, target):
        def find_first(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                earlier = find_first(left, mid - 1)
                return mid if earlier < 0 else earlier
            elif nums[mid] < target:
                return find_first(mid + 1, right)
            else:
                return find_first(left, mid - 1)
        
        def find_last(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                later = find_last(mid + 1, right)
                return mid if later < 0 else later 
            elif nums[mid] < target:
                return find_last(mid + 1, right) 
            else:
                return find_last(left, mid - 1)

        return [find_first(0, len(nums) - 1), find_last(0, len(nums) - 1)]

"""
O(n log n)
"""
class Solution(object):
    def searchRange(self, nums, target):
        result = []

        def binary_search(left, right):
            if left > right:
                return

            mid = (left + right) // 2

            if nums[mid] == target:
                result.append(mid)
                binary_search(mid + 1, right) 
                binary_search(left, mid - 1) 
            elif nums[mid] < target:
                binary_search(mid + 1, right) 
            else:
                binary_search(left, mid - 1)

        binary_search(0, len(nums) - 1)

        result.sort()
        return [result[0], result[-1]] if result else [-1, -1]

        