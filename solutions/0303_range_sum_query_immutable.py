"""
Approach 1: Brute Force

- Store the original array.
- Iterate from left to right and accumulate the sum.

Complexity:
- Initialization: O(1)
- sumRange: O(k), where k is the queried range length.
- Extra space: O(1)
"""
class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        
    def sumRange(self, left, right):
        result = 0
        for i in range(left, right + 1):
            result += self.nums[i]
        return result

"""
Approach 2: Prefix Sum

- Calculate all prefix sums during initialization and store them.
- Add an extra 0 at the beginning of the prefix_sum array.
- Use the difference between two prefix sums to calculate the range sum.

Complexity:
- Initialization: O(n)
- Each sumRange query: O(1)
- Extra space: O(n)
"""
class NumArray(object):

    def __init__(self, nums):
        self.prefix_sum = [0]

        for i, n in enumerate(nums):
            self.prefix_sum.append(n+self.prefix_sum[i])
        

    def sumRange(self, left, right):
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        