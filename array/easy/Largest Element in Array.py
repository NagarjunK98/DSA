'''
Given an array A[] of size n. The task is to find the largest element in it.

Input:
n = 5
A[] = {1, 8, 7, 56, 90}
Output:
90
Explanation:
The largest element of given array is 90.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

def largest( arr, n):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest