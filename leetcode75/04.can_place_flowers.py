'''
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

# Solution-1 - First approach

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if len(flowerbed) == 1:
            if flowerbed[i] == 0 and n >= 1:
                n = n - 1
                i = i + 1
            else:
                i = i + 1
        else:
            while i < len(flowerbed) and n > 0:
                if i == 0 and flowerbed[0] == 0:
                    if flowerbed[1] == 0:
                        flowerbed[0] = 1
                        i = i + 2
                        n = n - 1
                    else:
                        i = i + 1
                elif i == len(flowerbed)-1 and flowerbed[-1] == 0:
                    if  flowerbed[-2] == 0:
                        n = n - 1
                        flowerbed[i] = 1
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        n = n-1
                        flowerbed[i] = 1
                        i = i + 2 
                    else:
                        i = i+1
        return True if n == 0 else False    
    
# Solution-2: simplified solution of solution-1

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        else:
            for i in range(len(flowerbed)):
                if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n = n - 1
                    if n == 0:
                        return True
        return True if n == 0 else False    