'''
Given an array Arr of size N, print second largest distinct element from an array.

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

def print2largest(self,arr, n):
    flarge = arr[0]
    slarge = -1
    for i in range(1, len(arr)):
        if arr[i] > flarge:
            slarge = flarge
            flarge = arr[i]
        elif arr[i] < flarge and arr[i] > slarge:
            slarge = arr[i]
    return slarge