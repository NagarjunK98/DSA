'''
You are given an array Arr of size N. You need to find all pairs in the array that sum to a number K. If no such pair exists then output will be -1. The elements of the array are distinct and are in sorted order.

Note: (a,b) and (b,a) are considered same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.

Input:
n = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
K = 8
Output: 3
Explanation: We find 3 such pairs that sum to 8 (1,7) (2,6) (3,5)

Input:
n = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
K = 98 
Output: -1

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1)
'''

# Solution-1 First approach
'''
Algo steps:
    1. Find sum-a[i] for all elements and store it in dict along with index
    2. loop through all elements, and check if a[i] present in dict and index is not equal then count++ and 
    delete d[a[i]] and d[sum-a[i]]
    3. return count if > 0 else -1

TC = O(N)
SC = O(N)
'''
class Solution:
    def Countpair (self, arr, n, sum) : 
        d = {}
        for i in range(len(arr)):
            d[sum-arr[i]] = i
        
        count = 0
        
        for i in range(len(arr)):
            if arr[i] in d and d[arr[i]] != i:
                count += 1
                del d[arr[i]]
                del d[sum-arr[i]]
        return count if count > 0 else -1

# Solution -2 Optimized approach
'''
Algo steps:
    1. Init low=0, high=n-1
    2. Loop through list till low < high and check a[low]+a[high]=sum then count else if a[low]+a[high] < sum then low++ else high--
    3. return count if count > 0 else -1

TC = O(N)
SC = O(1)
'''
class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        low = 0
        high = n-1
        count = 0        
        while low < high:
            if arr[low]+arr[high] == sum:
                count += 1
                low += 1
                high -= 1
            elif arr[low]+arr[high] < sum:
                low += 1
            else:
                high -= 1
        return count if count > 0 else -1