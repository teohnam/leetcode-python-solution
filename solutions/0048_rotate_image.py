"""
Rotate 90 degrees clockwise == Flip across the main diagonal, then flip horizontally.
"""
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Swap elements below the main diagonal to transpose the matrix
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()