from collections import Counter

class Solution:
    def frequencySort(self, s):
        result = []

        frequency_dict = Counter(s)
        # frequency_dict = {}
        # for letter in s:
        #     if letter in frequency_dict:
        #         frequency_dict[letter] += 1
        #     else:
        #         frequency_dict[letter] = 1
        
        high_to_low = sorted(frequency_dict.keys(), key=lambda key: frequency_dict[key], reverse=True)

        for key in high_to_low:
            result.extend(key * frequency_dict[key])
        
        return "".join(result)
        