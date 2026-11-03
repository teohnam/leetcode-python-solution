class Solution(object):
    def spiralOrder(self, matrix):
        result = []

        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        while top <= bottom and left <= right:
            # Go right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Go down
            if left <= right:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1

            # Go left
            if left <= right and top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Go up
            if left <= right and top <= bottom:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result