'''
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

Examples 1:
Input:
 matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output:
 [[1,0,1],[0,0,0],[1,0,1]]

Explanation:
 Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input:
 matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:
[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:
Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
'''

# Solution-1: Brute force approach using list
'''
Alogrithm:
    1. find all zeros indexes(i, j) in matrix
    2. for each indexes, replace ith rows to zero and jth column to zero

If indexes have (0,0) & (0,3), then it will run twice for i=0 row. not optimal solution 

Time complexity = O(N*M)+(O(N*M)

Space complexity = O(N*M)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        j = 0
        indexes = []
        i = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    indexes.append([i, j])
        for index in indexes:
            i = index[0]
            j = index[1]
            for index in range(len(matrix[0])):
                matrix[i][index] = 0
            for index in range(len(matrix)):
                matrix[index][j] = 0

# Solution-2: Brute force approach using set
'''
Alogrithm:
    1. find all zeros indexes(x, y) in matrix and stores them in set separatly to avoid repitition
    2. for each indexes, replace ith rows to zero and jth column to zero

If zeros position have (0,0) & (0,3), then index_x = (0) & index_y = (0, 3). So multiple runs. Somewhat optimal solution

Time complexity = O(N*M)+O(N)+O(M)

Space complexity = O(N) + O(M)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        j = 0
        indexes_x = set()
        indexes_y = set()
        i = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    indexes_x.add(i)
                    indexes_y.add(j)
        for i in indexes_x:
            for index in range(len(matrix[0])):
                matrix[i][index] = 0
        for j in indexes_y:
            for index in range(len(matrix)):
                matrix[index][j] = 0
