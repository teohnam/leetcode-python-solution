class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if n== 0:
                break
            
            left_empty = i == 0 or flowerbed[i-1] == 0
            right_empty = i == len(flowerbed) -1 or flowerbed[i+1] == 0

            if flowerbed[i] == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
        
        return True if n <= 0 else False
        