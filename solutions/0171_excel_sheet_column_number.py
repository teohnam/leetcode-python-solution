import string


class Solution(object):
    def titleToNumber(self, columnTitle):
        letter_to_num = {letter: i for i, letter in enumerate(string.ascii_uppercase, start=1)}
        
        title_list = list(reversed(columnTitle))

        result = 0
        for index, title in enumerate(title_list):
            result += letter_to_num[title] * 26**index

        return result
        