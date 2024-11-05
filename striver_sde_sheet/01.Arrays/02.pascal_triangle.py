'''
Problem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.
'''

# Solution-1

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            temp_res = [1]
            for j in range(1,i):
                temp_res.append(res[i-1][j-1]+res[i-1][j])
            temp_res.append(1)
            res.append(temp_res)
        return res