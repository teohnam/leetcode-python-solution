import re

"""
Compare the first half of the string with the reversed second half.
"""
class Solution(object):
    def isPalindrome(self, s):
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        middle = len(cleaned_s) // 2
        
        first_half = cleaned_s[:middle]

        # Even number of digits: compare both halves
        # Odd number of digits: skip the middle letter
        if len(cleaned_s) % 2 == 0:
            second_half_reversed = cleaned_s[middle:][::-1]
        else:
            second_half_reversed = cleaned_s[middle+1:][::-1]
        
        return first_half == second_half_reversed

        