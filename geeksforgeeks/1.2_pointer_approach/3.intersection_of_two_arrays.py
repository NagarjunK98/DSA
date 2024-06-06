'''
Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the intersection (or common elements) of the two arrays.

For this question, the intersection of two arrays can be defined as the set containing distinct common elements between the two arrays

Input:
n = 5, m = 3
a[] = {89, 24, 75, 11, 23}
b[] = {89, 2, 4}

Output: 1

Explanation: 
89 is the only element 
in the intersection of two arrays.

Input:
n = 6, m = 5
a[] = {1, 2, 3, 4, 5, 6}
b[] = {3, 4, 5, 6, 7} 

Output: 4

Explanation: 
3 4 5 and 6 are the elements 
in the intersection of two arrays.

Input:
n = 5, m = 2
a[] = {2, 2, 2, 2, 2}
b[] = {2, 2} 

Output: 1

Explanation: 
2 is the common element in the intersection of two arrays. We count element only once

You don't need to read input or print anything. Your task is to complete the function NumberofElementsInIntersection() which takes two integers n and m and their respective arrays a[] and b[]  as input. The function should return the count of the number of elements in the intersection.

Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(n).
'''

# Solution-1 First approach - Time limit exceeded
'''
Algo Steps:
    1. Sort both a and b list in ascending order
    2. Init i=0 & j=0
    3. loop through both lists and increment counter if matched else increment based on condition

TC = O(nlogn)
SC = O(1)
'''
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        
        a.sort()
        b.sort()
        count = 0
        i =0
        j =0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                count+=1
                i+=1
                j+=1
            elif a[i] < b[j]:
                i+=1
            else:
                j+=1
        return count

# Solution-2 Optimized approach 
'''
Algo steps:
    1. Create a set of unique element of any list
    2. loop through other list and check if ele present in set if yes, then increment count & remove that element from set

TC = O(n)
SC = O(n)
'''
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        from collections import Counter
        ele_set = set(a)
        count = 0
        for ele in b:
            if ele in ele_set: 
                count+=1
                ele_set.remove(ele)
        return count