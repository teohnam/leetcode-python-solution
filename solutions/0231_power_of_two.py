"""
Opitmized solution

When n is a power of two, n and n - 1 have no set bits
in common in their binary representations.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

"""
A power of two is a positive integer with exactly one set bit
in its binary representation.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        def hammingWeight(n):
            hamming_weight = 0

            while (n > 0):
                hamming_weight += n % 2
                n //= 2
            
            return hamming_weight

        return  n > 0 and hammingWeight(n) == 1