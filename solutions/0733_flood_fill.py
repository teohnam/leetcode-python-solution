"""
DFS (Depth-First Search):
Explore as far as possible along each path before backtracking.
"""
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        origin_color = image[sr][sc]

        # Prevent infinite recursion when the new color is the same as the original color.
        if origin_color == color:
            return image

        def fill(sr, sc):
            out_of_bounds = sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr])
            # Stop if the current pixel is out of bounds or doesn't have the original color.
            if out_of_bounds or image[sr][sc] != origin_color:
                return
            
            image[sr][sc] = color
            # Recursively explore the four neighboring pixels of the current pixel.
            fill(sr-1, sc)
            fill(sr+1, sc)
            fill(sr, sc-1)
            fill(sr, sc+1)
            
        fill(sr, sc)
        return image
        