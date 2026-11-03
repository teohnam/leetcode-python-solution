"""
Backtracking
"""
class Solution(object):
    def combine(self, n, k):
        result = []

        def recursive(index, path):
            path.append(index)

            if len(path) == k:
                result.append(path[:])
                # After exploring a branch, remove its last element so the next branch starts with the correct path.
                path.pop()
                return

            for i in range(index + 1, n - k + len(path) + 2):
                recursive(i, path)

            path.pop()

        for i in range(1, n - k + 2):
            recursive(i, [])

        return result