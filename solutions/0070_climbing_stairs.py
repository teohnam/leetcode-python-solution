"""
Dynamic Programming (Bottom-Up DP)
Store previously calculated results to avoid redundant calculations.

- Time complexity: (O(n)) — each result is calculated once.
- Space complexity: (O(n)) — the list stores all intermediate results.
"""
class Solution(object):
    def climbStairs(self, n):
        dp = []

        for i in range(n):
            if i == 0:
                dp.append(1)
            elif i == 1:
                dp.append(2)
            else:
                dp.append(dp[i-1] + dp[i-2])

        return dp[n-1]

"""
Recursive Solution
Calculate the result by recursively solving smaller subproblems. This implementation recalculates the same subproblems multiple times.

- Time complexity: (O(2^n)) — exponential time in the worst case.
- Space complexity: (O(n)) — the maximum recursion depth is proportional to n.
"""
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)