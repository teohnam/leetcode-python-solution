"""
Kadane's algorithm
O(n)
"""
class Solution(object):
    def maxSubArray(self, nums):
        max_ending = nums[0]
        result = nums[0]
        for index in range(len(nums)):
            max_ending = max(max_ending + nums[index], nums[index])
            result = max(result, max_ending)
        return result

"""
O(n**2)
"""
class Solution(object):
    def maxSubArray(self, nums):
        sum_list = []
        for index, num  in enumerate(nums):
            sum_sub = 0
            for i in range(index, len(nums)):
                sum_sub += nums[i]
                sum_list.append(sum_sub)
        
        return max(sum_list)