"""
Hamming Weight: the number of set bits (1s) in a number's binary representation.

Logic:
1. Divide the number by 2 and get the remainder.
2. The remainder is the rightmost bit (0 or 1) of the binary representation.
3. Add the remainder to the count.
4. Divide the number by 2 using integer division to remove the rightmost bit.
5. Repeat until the number becomes 0.
"""
class Solution(object):
    def hammingWeight(self, n):
        hamming_weight = 0

        while (n > 0):
            hamming_weight += n % 2
            n //= 2
        
        return hamming_weight

        

        