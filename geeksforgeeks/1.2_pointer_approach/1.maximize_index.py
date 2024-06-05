'''
Given an array a of n positive integers. The task is to find the maximum of j - i subjected to the constraint of a[i] < a[j] and i < j.

The task is to complete the function maxIndexDiff() which takes array a[] and integer n as input and returns the maximum index difference

Input:
n = 2
a[] = {1, 10}
Output:
1
Explanation:
a[0] < a[1] so (j-i) is 1-0 = 1.

Input:
n = 9
a[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array a[1] < a[7] satisfying the required condition(a[i] < a[j]) thus giving the maximum difference of j - i which is 6(7-1).

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
'''
# Solution-1 - First approach TC=O(N^2) - Time limit exceeded
class Solution:
    def maxIndexDiff(self,a, n): 
        
        max_value = 0
        
        for i in range(0,n):
            ele = i
            for j in range(n-1,i-1,-1):
                if a[i] <= a[j]:
                    max_value = max(max_value, j-i)
        return max_value


# Solution-2 - 2 pointer approach.
'''
Algo steps:
    1. First create an empty array of length n and initialize last element of array to last element of original array
    2. From the right side, loop through each index and find max till that index and store it
    3. Init i=0, & j=0
    4. Loop through i<n and j<n, and check if a[i] <= new_array[j] if yes j++ else i++ and find max(j-i) 

TC=O(N)
SC=O(N)
'''
class Solution:
    def maxIndexDiff(self,a, n): 
        
        max_index = 0
        i = 0
        j = 0
        right_max_value = [0]*n
        right_max_value[-1] = a[-1]
        
        for i in range(n-2,-1,-1):
            right_max_value[i] = max(right_max_value[i+1],a[i])
        
        while i < n and j < n:
            if a[i] <= right_max_value[j]:
                max_index = max(max_index, j-i)
                j+=1
            else:
                i+=1
        return max_index
        

# Related problem - Instead of max(j-i), find max(a[j]-a[i]) where i < j and a[j] > a[i]
'''
Algo steps:
    1. First create an empty array of length n and initialize last element of array to last element of original array
    2. From the right side, loop through each index and find max till that index and store it
    3. Init i=0, & j=0
    4. Loop through i<n and j<n, and check if a[i] < new_array[j] if yes i++ else j++ and find max(new_array[j]-a[i]) 

TC=O(N)
SC=O(N)
'''
def maxValueDiff(a, n): 
        
    max_value = 0
    i = 0
    j = 0
    right_max_value = [0]*n
    right_max_value[-1] = a[-1]
    
    for i in range(n-2,-1,-1):
        right_max_value[i] = max(right_max_value[i+1],a[i])
    
    while i < n and j < n:
        if a[i] < right_max_value[j]:
            max_value = max(max_value, right_max_value[j]-a[i])
            i+=1
        else:
            j+=1
    return max_value