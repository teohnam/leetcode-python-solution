"""
Divide and Conquer
Time: O(n log n)
Space: O(log n) for the recursion stack
"""
class Solution(object):
    def maxSubArray(self, nums):
        def max_subarray_sum(left, right):
            # Base case: a subarray containing one element.
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # Find the maximum suffix sum of the left half.
            # The suffix must end at mid.
            max_suffix = nums[mid]
            suffix = nums[mid]
            for i in range(mid - 1, left - 1, -1):
                suffix += nums[i]
                max_suffix = max(max_suffix, suffix)

            # Find the maximum prefix sum of the right half.
            # The prefix must start at mid + 1.
            max_prefix = nums[mid + 1]
            prefix = nums[mid + 1]
            for i in range(mid + 2, right + 1):
                prefix += nums[i]
                max_prefix = max(max_prefix, prefix)

            # The maximum subarray is entirely in the left half,
            # entirely in the right half, or crosses the midpoint.
            left_max = max_subarray_sum(left, mid)
            right_max = max_subarray_sum(mid + 1, right)
            cross_max = max_suffix + max_prefix

            return max(left_max, right_max, cross_max)

        return max_subarray_sum(0, len(nums) - 1)

"""
Kadane's Algorithm
Time: O(n)
Space: O(1)

At each element, either extend the current subarray
or start a new subarray from the current element.
Track the maximum sum found so far.
"""
class Solution(object):
    def maxSubArray(self, nums):
        max_ending = nums[0]
        result = nums[0]

        for index in range(1, len(nums)):
            # Extend the current subarray or start a new one.
            max_ending = max(max_ending + nums[index], nums[index])

            # Update the overall maximum sum.
            result = max(result, max_ending)

        return result

"""
Brute Force
Time: O(n^2)
Space: O(1) auxiliary space

Enumerate every possible subarray and track its sum.
Keep the maximum sum without storing all subarray sums.
"""
class Solution(object):
    def maxSubArray(self, nums):
        result = nums[0]

        for index in range(len(nums)):
            sum_sub = 0
            for i in range(index, len(nums)):
                sum_sub += nums[i]
                result = max(result, sum_sub)

        return result