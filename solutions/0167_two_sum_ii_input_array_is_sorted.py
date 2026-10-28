"""
Two pointers

Use left and right to point to elements in the array, moving the pointers accordingly.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        sum = numbers[left] + numbers[right]
        while left < right:
            if sum > target:
                right -= 1
                sum = numbers[left] + numbers[right]
            elif sum < target:
                left += 1
                sum = numbers[left] + numbers[right]
            else:
                # Problem requires 1-based indices.
                return [left + 1, right + 1]

        