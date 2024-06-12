'''
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: 
Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.

Your task is to complete the function countDistinct() which takes the array A[], the size of the array(N) and the window size(K) as inputs and returns an array containing the count of distinct elements in every contiguous window of size K in the array A[].

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
'''

# Solution - 1 First approach
'''
Algo steps:
    1. Init result list, counter to track window size and dict to hold frequency of each char
    2. loop through list
        2.1 increment counter
        2.2 update dict frequency
        2.3 check if counter = K then append length of dict to result list
        2.4 if frequency of first element of window is > 1 then decrement else del the dict instance
    3. return result list

TC = O(N)
SC = O(N)  
'''
class Solution:
    def countDistinct(self, A, N, K):
        res = []
        counter = 0
        d = {}
        for i in range(N):
            counter += 1
            
            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1
                    
            if counter == K:
                res.append(len(d))
                f_ele = A[i-K+1]
                counter -= 1
                if d[f_ele] > 1:
                    d[f_ele] -= 1
                else:
                    del d[f_ele]
        return res 