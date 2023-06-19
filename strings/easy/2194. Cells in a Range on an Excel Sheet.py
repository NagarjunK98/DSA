'''
A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:

<col> denotes the column number c of the cell. It is represented by alphabetical letters.
For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
<row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1, 
<row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as 
strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.

Input: s = "K1:L2"
Output: ["K1","K2","L1","L2"]
'''

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        start_col = start[0]
        start_row = int(start[1])
        end_col = end[0]
        end_row = int(end[1])
        l = []
        for i in range(ord(start_col), ord(end_col)+1):
            for j in range(start_row, end_row+1):
                l.append(chr(i)+str(j))    
        return l    

