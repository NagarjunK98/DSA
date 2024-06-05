'''
Given a sorted array a[] of size n, delete all the duplicated elements from a[] & modify the array such that only distinct elements should be present there.

Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size where only distinct elements are present in the array, the driver code will print all the elements of the modified array.

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 
1
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. {2} so modify array will contains 2 at first position and you should return 1 after modify the array.

Input:
N = 4
Array = {1, 2, 2, 4}
Output: 3
Explanation: After removing all duplicates modify array will contains {1, 2, 4} at first 3 positions so you should return 3 after modify the array.

Your Task:  
You don't need to read input or print anything. Complete the function remove_duplicate() which takes the array a[] and its size n as input parameters and modifies it in place to delete all the duplicates. The function must return an integer X denoting the no. of distinct elements in the array keeping the first X elements of an array in increasing order. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

# Solution-1 First approach - Using HashMap counter
'''
Algo steps:
    1. Apply collections Counter on input list to find frequency of each element
    2. loop through counter dict and if v>1 to remove duplicates from original list
    3. return length of modified list 

TC = O(N*M)
SC = O(N)
'''
class Solution:	
    def remove_duplicate(self, A, N):
        from collections import Counter
        
        counter = Counter(A)

        for k,v in counter.items():
            if v > 1:
                for j in range(1,v):
                    A.remove(k)
        return len(A)

# Solution-2  2 pointer approach - Optimized approach
'''
Algo steps:
    1. Init left=0 & right=1
    2. loop though list till right < len(A) and check if A[left]==A[right] then remove A(right)
    3. else assign left=right and increment right by 1

TC = O(N)
SC = O(1)
'''
class Solution:	
    def remove_duplicate(self, A, N):
        left = 0
        right = 1
        while right < len(A):
            if A[left] == A[right]:
                A.remove(A[right])
            else:
                left = right
                right += 1
        return len(A)