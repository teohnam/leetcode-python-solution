"""
Built-in sorting + custom comparator
Time: O(n log n * k)
Space: O(nk)
"""
from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        strings = [str(n) for n in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        strings.sort(key=cmp_to_key(compare))

        return "".join(strings).lstrip('0') or '0'

"""
Insertion sort
Time: O(n^2 * k)
Space: O(nk)
"""
class Solution(object):
    def largestNumber(self, nums):
        strings = [str(n) for n in nums]

        for i in range(1, len(strings)):
            while i > 0:
                if strings[i] + strings[i - 1] > strings[i - 1] + strings[i]:
                    strings[i - 1], strings[i] = strings[i], strings[i - 1]
                    i -= 1
                else:
                    break

        return "".join(strings).lstrip('0') or '0'
