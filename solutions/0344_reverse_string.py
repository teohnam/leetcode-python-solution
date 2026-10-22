"""
An in-place algorithm modifies the input in place, without creating a separate copy of the data structure.
"""

"""
Original solution: swap elements using a temporary variable.
"""
class Solution(object):
    def reverseString(self, s):
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
        return s


"""
Simplified version: use Python's multiple assignment to swap elements.
"""
class Solution(object):
    def reverseString(self, s):
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]