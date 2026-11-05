"""
O(n log(n))
"""
import bisect
class Solution(object):
    def minSubArrayLen(self, target, nums):
        prefix = [0]
        min_len = float('inf')

        for n in nums:
            prefix.append(prefix[-1] + n)

        for i in range(len(prefix)):
            # Find the first index where prefix[idx] >= prefix[i] + target
            idx = bisect.bisect_left(prefix, prefix[i] + target)
            
            # Only update if a valid upper bound index was found
            if idx < len(prefix):
                min_len = min(min_len, idx - i)

        return min_len if min_len != float('inf') else 0
        


"""
O(n)
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left_pointer = 0
        window_sum = 0
        min_len = float('inf')

        for i in range(len(nums)):
            window_sum += nums[i]
            while window_sum >= target:
                min_len = min(min_len, i - left_pointer + 1)
                window_sum -= nums[left_pointer]
                left_pointer += 1

        return min_len if min_len != float('inf') else 0



        