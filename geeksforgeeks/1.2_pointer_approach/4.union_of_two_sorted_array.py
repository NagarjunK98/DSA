'''
Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 5, arr2 [] = {1, 2, 3, 6, 7}
Output: 
1 2 3 4 5 6 7
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5 6 7

Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 
1 2 3 4 5
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5.

n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 
1 2
Explanation: 
Distinct elements including both the arrays are: 1 2.

Your Task: 
You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays.

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
'''

# Solution -1 First approach
'''
Algo steps:
    1. Init i=0 & j=0. Create a empty set to track which element are added to result list
    2. Loop through both lists till last element and if both are equal add ele and increment i &j. If arr1[i] < arr2[j], then add arr1[i] and increment i else add arr2[j] and increment j
    3. Add conditional append to check if all elements are being covered in both lists or not
'''
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        
        i = 0
        j = 0
        res = []
        tracker = set()
        while i < n or j < m:
            if(i < n and j < m):
                if arr1[i] == arr2[j]:
                    if arr1[i] not in tracker:
                        res.append(arr1[i])
                        tracker.add(arr1[i])
                    i+=1
                    j+=1
                elif arr1[i] < arr2[j]:
                    if arr1[i] not in tracker:
                        res.append(arr1[i])
                        tracker.add(arr1[i])
                    i+=1
                else:
                    if arr2[j] not in tracker:
                        res.append(arr2[j])
                        tracker.add(arr2[j])
                    j+=1
            elif i < n:
                if arr1[i] not in tracker:
                    res.append(arr1[i])
                    tracker.add(arr1[i])
                i+=1
            else:
                if arr2[j] not in tracker:
                    res.append(arr2[j])
                    tracker.add(arr2[j])
                j+=1
                
        return res