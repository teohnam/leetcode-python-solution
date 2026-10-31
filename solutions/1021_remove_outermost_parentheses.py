"""
Keep parentheses at depth 2 and above
"""
class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        count = 0
        for p in s:
            if p == "(":
                count += 1
                if count > 1:
                    result.append(p)
            else:
                count -= 1
                if count > 0:
                    result.append(p)

        return "".join(result)