"""
Optimized Solution
Time: O(n)
Space: O(n)

Instead of searching the remaining list for a matching number,
store previously visited numbers in a dictionary. 
For each new number, check whether a previously stored number plus the current number equals the target.
"""
class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index


"""
Brute-Force Solution
Time: O(n^2)
Space: O(1)
"""
class BruteForceSolution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]
