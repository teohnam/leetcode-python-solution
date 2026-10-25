"""
Optimized version
Build the result using a list and append each digit.
This avoids repeatedly creating new strings when prepending digits,
reducing the time complexity from O(k^2) to O(k),
where k = max(len(a), len(b)).
"""
class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        result = []
        n = len(a)
        m = len(b)
        
        for i in range(max(n, m)):
            digit_a = int(a[n - 1 - i]) if i < n else 0
            digit_b = int(b[m - 1 - i]) if i < m else 0

            total = digit_a + digit_b + carry

            result.append(str(total % 2))
            carry = total // 2

        if carry == 1:
            result.append('1')

        result.reverse()
        return ''.join(result)


"""
Original solution
"""
class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        result = ''
        n = len(a)
        m = len(b)
        
        for i in range(max(n, m)):
            digit_a = int(a[n - 1 - i]) if i < n else 0
            digit_b = int(b[m - 1 - i]) if i < m else 0

            total = digit_a + digit_b + carry

            # Prepending to a string creates a new string each time
            result = str(total % 2) + result
            carry = total // 2

        if carry == 1:
            result = '1' + result

        return result