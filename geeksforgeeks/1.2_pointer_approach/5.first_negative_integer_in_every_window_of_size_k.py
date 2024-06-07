'''
Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function printFirstNegativeInteger() which takes the array A[], its size N and an integer K as inputs and returns the first negative number in every window of size K starting from the first till the end. If a window does not contain a negative integer , then return 0 for that window.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)
'''
# Solution -1 - First approach
'''
Algo steps:
    1. Init res list to store result, neg_arr to store negative values, neg_index to store negative value index and counter=1
    2. Loop through list, if A[i] < 0 add to neg_arr and neg_index
    3. If counter = K, then check if any negative element present in the window, if yes add neg_arr[0] to res list else append 0. And Once we pass the current window, delete the neg_arr[0] and neg_index by checking neg_index[0]+(K-1) == i. Again reinitialize counter=K-1  
'''
def printFirstNegativeInteger( A, N, K):
    res = []
    counter = 1
    neg_arr = []
    neg_index = []
    for i in range(0,N):
        if A[i] < 0:
            neg_arr.append(A[i])
            neg_index.append(i)
        if counter == K:
            if len(neg_arr) == 0:
                res.append(0)
            else:
                res.append(neg_arr[0])
                if neg_index[0]+(K-1) == i:
                    neg_arr.pop(0)
                    neg_index.pop(0)
            counter = K - 1
        counter+=1
    return res