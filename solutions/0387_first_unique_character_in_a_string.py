class Solution(object):
    def firstUniqChar(self, s):
        letter_to_count = {}

        for letter in s:
            if letter in letter_to_count:
                letter_to_count[letter] += 1
            else:
                letter_to_count[letter] = 1

        for index, letter in enumerate(s):
            if letter_to_count[letter] == 1:
                return index

        return -1

        