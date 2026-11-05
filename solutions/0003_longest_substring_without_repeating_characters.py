"""
Sliding Window + Dictionary

Use a dictionary to store each character's latest index.
When a duplicate is found, move left_pointer to the position
after its previous occurrence.

Time: O(n) average
Space: O(min(n, k)), where k is the character set size.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left_pointer = 0
        max_len = 0

        for i in range(len(s)):

            if s[i] in char_index:
                left_pointer = max(left_pointer, char_index[s[i]] + 1)

            char_index[s[i]] = i
            max_len = max(max_len, i + 1 - left_pointer)

        return max_len

"""
Original solution

Time:O(n2)
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unique_s = []
        left_pointer = 0
        max_len = 0

        for i in range(len(s)):

            if s[i] in unique_s:
                left_pointer += unique_s.index(s[i]) + 1

            unique_s = s[left_pointer:i+1]
            max_len = max(max_len, len(unique_s))

        return max_len
