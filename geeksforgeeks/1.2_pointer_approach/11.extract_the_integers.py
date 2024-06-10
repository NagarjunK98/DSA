'''
Given a string s, extract all the integers from s.

Input:
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 
     3: Rishabh Gupta56"
Output: 1 2 3 56
Explanation: 
1, 2, 3, 56 are the integers present in s

Input:
s = "geeksforgeeks"
Output: No Integers
Explanation: 
No integers present in the string.

You don't need to read input or print anything. Complete the function extractIntegerWords() which takes string s as input and returns a list of strings. If an empty list is returned the output is printed as "No Integers".

Expected Time Complexity: O(|s|).
Expected Auxiliary Space: O(|s|).
'''

# Solution-1 First approach
'''
Algo steps:
    1. Init result list, curr_index & last_index to tract starting of integer and ending of integer(in case of more than single digits) and set flag = False
    2. loop through each string character and check if it is numeric or not
        2.1 if yes, then set curr_index = i and last_index = i and set flag = True
        2.2 in case of more than single digits, then check if flag=True, then assign new index to last_index
        2.3 If not numeric, check flag=True then append s[current_index : last_index+1] to result list
    3. return list
'''
class Solution:

    def extractIntegerWords(self, s):
        # code here
        res = []
        curr_index = 0
        last_index = 0
        flag = False
        for i in range(len(s)):
            if s[i].isnumeric():
                if flag:
                    last_index = i
                else:
                    curr_index = i
                    last_index = i
                    flag = True
            else:
                if flag:
                    res.append(s[curr_index:last_index+1])
                    flag = False
        if flag:
            res.append(s[curr_index:last_index+1])
        return res