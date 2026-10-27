class Solution(object):
    def romanToInt(self, s):
        result = 0

        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for index, numeral in enumerate(s):
            # If the current numeral is smaller than the next one, subtract its value; otherwise, add it.
            if index < len(s) - 1 and roman_values[numeral] < roman_values[s[index + 1]]:
                result -= roman_values[numeral]
            else: 
                result += roman_values[numeral]

        return result
                
        