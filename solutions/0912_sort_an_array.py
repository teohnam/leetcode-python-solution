"""
Merge Sort — Divide and Conquer

Complexity:
- Time: O(n log n)
- Space: O(n) auxiliary space
"""
class Solution(object):
    def sortArray(self, nums):
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            # Divide: Split the array into two halves.
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            # Conquer
            return merge(left, right)

        # Combine: Merge the two sorted halves.
        def merge(left, right):
            left_pointer = 0
            right_pointer = 0
            merged_result = []

            while left_pointer < len(left) and right_pointer < len(right):
                if left[left_pointer] < right[right_pointer]:
                    merged_result.append(left[left_pointer])
                    left_pointer += 1
                else:
                    merged_result.append(right[right_pointer])
                    right_pointer += 1

            merged_result.extend(left[left_pointer:])
            merged_result.extend(right[right_pointer:])

            return merged_result

        return mergeSort(nums)