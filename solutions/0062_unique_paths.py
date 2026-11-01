"""
Math: Combinatorics (Python 3)

Time: O(min(m, n)) approximately
Space: O(1) auxiliary space
"""
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, n-1)

"""
Dynamic Programming (2D)

dp[i][j] = dp[i-1][j] + dp[i][j-1]

Time: O(m * n)
Space: O(m * n)
"""
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[None for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n - 1][m - 1]

                
        
        