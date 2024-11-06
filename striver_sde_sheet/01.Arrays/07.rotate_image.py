'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

n == matrix.length == matrix[i].length
'''

# Solution-1: Brute force solution
'''
Algorithm:
    1. initialize empty list
    2. loop through row & column and append to list

Time complexity = O(N2)
Space complexity = O(N2)
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        res = []
        for i in range(0,n):
            temp= []
            for j in range(n-1, -1, -1):
                temp.append(matrix[j][i])
            res.append(temp)
        print(res)
