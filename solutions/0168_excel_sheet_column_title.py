"""
Subtract 1 to handle Excel's 1-based numbering system,
where A = 1 and Z = 26, instead of 0-based digits.
"""
import string


class Solution(object):
    def convertToTitle(self, columnNumber):
        num_to_letter = {i: letter for i, letter in enumerate(string.ascii_uppercase)}

        result = []
        while columnNumber > 0:
            result.append(num_to_letter[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26

        result.reverse()
        return "".join(result)
                
        