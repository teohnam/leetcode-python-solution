"""
Three conditions:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""
class Solution(object):
    def isValid(self, s):
        parentheses_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        # Tracks opening brackets so each closing bracket is checked against the most recently opened one.
        stack = []

        for parenthesis in s:
            if parenthesis in parentheses_dict:
                stack.append(parenthesis)

            elif parenthesis in parentheses_dict.values():
                # Checks Condition 1 & 3
                if stack and parenthesis == parentheses_dict[stack[-1]]:
                    stack.pop()
                else:
                    return False

        # Checks Condition 1 & 2
        return not stack