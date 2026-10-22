"""
Reverse half of the number.
"""
class Solution(object):
    def isPalindrome(self, x):
        # Reject negative numbers and nonzero numbers ending in 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Stop when the reversed half has at least as many digits as the remaining half
        while x > reversed_half:
            # Append the last digit of x to the reversed half
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even number of digits: compare both halves
        # Odd number of digits: ignore the middle digit
        return x == reversed_half or x == reversed_half // 10

"""
Reverse the entire number recursively and compare it with the original.
"""
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        def reverse(n, reversed_num=0):
            if n == 0:
                return reversed_num

            return reverse(n // 10, reversed_num * 10 + n % 10)

        return reverse(x) == x
        
        
        