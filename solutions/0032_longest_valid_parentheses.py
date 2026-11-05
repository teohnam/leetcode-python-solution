class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        result = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                # When there is an unmatched closing parenthesis, the stack becomes empty.
                # Push its index as the new boundary.
                if not stack:
                    stack.append(i)
                else:
                    # The top of the stack represents the index immediately before
                    # the current valid contiguous substring.
                    length = i - stack[-1]
                    result = max(result, length)
        
        return result


        