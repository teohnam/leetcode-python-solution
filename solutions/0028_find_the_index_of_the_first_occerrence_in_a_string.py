class Solution(object):
    def strStr(self, haystack, needle):
        # Iterate only through valid starting positions
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index] == needle[0] and haystack[index : index + len(needle)] == needle:
                return index

        return -1