'''
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

All the characters of String S lies in the set {'0', '1', '2'}

Input:
S = 10212
Output:
3
Explanation:
The substring 102 is the smallest substring that contains the characters 0, 1 and 2.

S = 12121
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.

Complete the function smallestSubstring() which takes the string S as input, and returns the length of the smallest substring of string S that contains all the three characters 0, 1 and 2.

Expected Time Complexity: O( length( S ) )
Expected Auxiliary Space: O(1)
'''

# Solution-1 First approach
'''
Algo steps:
    1. Init zero, one two to -1 as staring point
    2. Loop through each char and check and assign index to respective number
    3. if zero, one, and two index are modified then find min(prev_res, max()-min())
    4. return result based on flag 
'''
class Solution:
    def smallestSubstring(self, S):
        import sys
        zero = -1
        one = -1
        two = -1
        res = sys.maxsize
        flag = False
        for i in range(len(S)):
            if S[i] == '0':
                zero = i
            elif S[i] == '1':
                one = i
            else:
                two = i
            
            if zero != -1 and one != -1 and two != -1:
                flag = True
                res = min(res, (max(zero, one, two)-min(zero, one, two)+1))
        return -1 if flag == False else res