'''
Find the repeating and missing numbers

Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

Example 1:
Input Format:  array[] = {3,1,2,5,3}
Result : {3,4)
Explanation : A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing

Example 2:
Input Format: array[] = {3,1,2,5,4,6,7,5}
Result: {5,8)
'''

# Solution-1:
'''
Algorithm:
    1. initialize a dictionary
    2. loop through array and if ele not in dict add it. if ele present in dict mark that as repeating no
    3. loop through (1, len(arr)) and check ele is present or not, if not present mark that as missing no

Time complexity = O(2N)
Space complexity = O(N)
'''


def find_missing_and_repeated_no(arr):
    d = {}
    
    missing_no = 0
    repeated_no = 0
    for ele in arr:
        if ele not in d:
            d[ele] = 1
        else:
            repeated_no = ele
    
    for ele in range(1, len(arr)+1):
        if ele not in d:
            missing_no = ele
            break
    
    return [repeated_no, missing_no]