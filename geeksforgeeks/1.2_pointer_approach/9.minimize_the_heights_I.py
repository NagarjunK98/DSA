'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once.

Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11. 

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
'''

# Solution -1 First approach
'''
We need to minimize the max difference

Algo steps:
    1. First sort the list elements
    2. Init min_ele = arr[0]+k, max_ele = arr[-1]-k, and initial result as arr[-1] - arr[0]
    3. loop through each element and 
        3.1. Decrement next element by k and check with previous min_ele to find minimum
        3.2. Increment current by k and check with previous max_ele to find maximum
        3.3. If min_temp > 0 then find min(res, max_ele - min_ele) as result

TC = O(nlogn)
SC = O(1)
'''

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        min_ele = arr[0] + k
        max_ele = arr[-1] - k
        res = arr[-1] - arr[0]
        for i in range(0, n-1):
            min_temp = min(min_ele, arr[i+1]-k)
            max_temp = max(max_ele, arr[i]+k)
            if min_temp < 0:
                continue
            else:
                res = min(res, max_temp-min_temp)
        return res