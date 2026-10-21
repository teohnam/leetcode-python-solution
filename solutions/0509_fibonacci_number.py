class Solution:
    # Approach 1: Direct recursion
    def fib(self, n):
        # f(0)
        if n == 0:
            return 0
        # f(1)
        if n == 1:
            return 1
        # f(n) = f(n-1) + f(n-2)
        if n > 1:
            return self.fib(n - 1) + self.fib(n - 2)


class SolutionSimplified:
    # Approach 2: Simplified recursion
    def fib(self, n):
        return n if n < 2 else self.fib(n - 1) + self.fib(n - 2)
