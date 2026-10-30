"""
Optimized solution using two pointers.
Time: O(n log n + m log m)
Space: O(n + m) for the sorted copies.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        children = sorted(g)
        cookies = sorted(s)
        
        child_index = 0
        cookie_index = 0

        while child_index < len(children) and cookie_index < len(cookies):
            if children[child_index] <= cookies[cookie_index]:
                # The cookie satisfies this child.
                child_index += 1

            # Move to the next one.
            cookie_index += 1

        return child_index
        

"""
Original greedy solution.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        result = 0
        for child in sorted(g):
            for cookie in sorted(s):
                if cookie >= child:
                    result += 1
                    s.remove(cookie)
                    break
        
        return result