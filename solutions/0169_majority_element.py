"""
Sorting Solution
s
Sort the array and return the middle element.
Since the majority element appears more than half of the time,
it must occupy the middle position in the sorted array.

Complexity:
Time: O(n log n) — sorting the array.
Space: O(n) — Python's sorting algorithm may require temporary space.
"""
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

"""
Boyer-Moore Majority Voting Algorithm
Use candidate to store the current potential majority element.
Use votes to track its net vote count.

Since the majority element appears more than half of the time,
its occurrences cannot all be cancelled out by other elements.
Therefore, the final candidate must be the majority element.

Complexity:
Time: O(n) — one pass through the array.
Space: O(1) — only two variables.
"""
class Solution(object):
    def majorityElement(self, nums):
        candidate = 0
        votes = 0

        for num in nums:
            if votes == 0:
                candidate = num

            if num == candidate:
                votes += 1
            else:
                votes -= 1

        return candidate
