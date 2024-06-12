'''
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Note - A subarray is a contiguous part of any given array.

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.

Input:
N = 4, K = 4
Arr = [100, 200, 300, 400]
Output:
1000
Explanation:
Arr1 + Arr2 + Arr3 + Arr4 =1000,
which is maximum.

You don't need to read input or print anything. Your task is to complete the function maximumSumSubarray() which takes the integer K, vector Arr with size N, containing the elements of the array and returns the maximum sum of a subarray of size K.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

# Solution - 1 First approach
'''
Algo steps:
    1. Init result max_sum=0, counter to track window size and running_sum to hold running total of all elements
    2. loop through list
        2.1 increment counter
        2.2 update running_sum
        2.3 check if counter = K then find max(max_sum, running_sum)
        2.4 subtract first ele value of each window from running_sum 
    3. return max_sum

TC = O(N)
SC = O(1)
'''
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        max_sum = 0
        counter = 0
        running_sum = 0
        for i in range(N):
            counter += 1
            running_sum += Arr[i]
            
            if counter == K:
                max_sum = max(max_sum, running_sum)
                first_window_value = Arr[i-K+1]
                running_sum -= first_window_value
                counter -= 1
        return max_sum