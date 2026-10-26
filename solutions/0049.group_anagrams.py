"""
Group anagrams using a dictionary.

Key: sorted letters of each word
Value: list of words with the same sorted letters

Example:
aet: ["eat", "tea", "ate"]
ant: ["tan", "nat"]
abt: ["bat"]
"""
class Solution(object):
    def groupAnagrams(self, strs):
        strs_dict = {}
        for str in strs:
            sorted_str = "".join(sorted(str))

            if sorted_str not in strs_dict:
                strs_dict[sorted_str] = []

            strs_dict[sorted_str].append(str)

        return list(strs_dict.values())