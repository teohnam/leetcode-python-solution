"""
Time: (O(mn))
Space: (O(1))
"""
class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check whether the first row contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check whether the first column contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use the first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out marked rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Zero out marked columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle the first row and column separately
        if first_row_zero:
            matrix[0] = [0] * n

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

"""
space: O(m+n)
"""
class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        r = []
        c = []

        for i in range(m):
            if not all(matrix[i]):
                r.append(i)

        for j in range(n):
            result = True
            for i in range(m):
                result = result and bool(matrix[i][j])
            if not result:
                c.append(j)

        if r:
            for i in r:
                for j in range(n):
                    matrix[i][j] = 0

        if c:
            for j in c:
                for i in range(m):
                    matrix[i][j] = 0
        