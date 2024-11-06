'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

# Solution-1
'''
Time complexity = O(N)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], nums[i]+cur_sum)
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
    
# Follow up question - Print subarray along with max subarray sum


import sys

def maxSubarraySum(arr, n):
    max_sum = -sys.maxsize - 1  # maximum sum
    cur_sum = 0

    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if cur_sum == 0:
            start = i  # starting index

        cur_sum += arr[i]

        if cur_sum > max_sum:
            max_sum = cur_sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if cur_sum < 0:
            cur_sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)

