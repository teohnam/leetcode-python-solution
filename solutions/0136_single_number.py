class Solution(object):
    def singleNumber(self, nums):
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        return next(key for key, value in nums_dict.items() if value == 1)

"""
XOR: Exclusive OR
A logical operation that takes two bits and returns 1 if they are different, and 0 if they are the same.
"""
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        
        return result