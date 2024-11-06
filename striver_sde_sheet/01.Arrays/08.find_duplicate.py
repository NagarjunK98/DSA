'''
287. Find the Duplicate Number

Find the duplicate in an array of N+1 integers

Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number, your task is to find the duplicate number.

Example 1: 

Input: arr=[1,3,4,2,2]

Output: 2

Explanation: Since 2 is the duplicate number the answer will be 2.

Example 2:

Input: [3,1,3,4,2]

Output:3

Explanation: Since 3 is the duplicate number the answer will be 3.
'''

# Solution-1: Brute force
'''
Algorithm:
    1. sort the array
    2. check a[i]==a[i+1] return ele 

Time complexity: O(NlogN)+O(N) 
'''

def find_duplicate(arr):
    arr.sort()

    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            return arr[i]

# Solution-2: optimal approach
'''
Algorithm:
    1. track elements in dict
    2. if element not in dict, add to dict else return ele as duplicate

Time complexity: O(N)
Space complexity: O(N) 
'''
def find_duplicate(arr):
    d = {}

    for ele in arr:
        if ele not in d:
            d[ele] = 1
        else:
            return ele