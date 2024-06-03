'''
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''

# Solution-1 - First Approach - Time limited Exceeded
'''
Sliding window problem
if len(nums) == k return sum(nums)/k as result. else loop through nums list from 0 to len(nums)-k+1.
In every iteration, calculate sum from i to i+k index and find average.
This approach involves reputation of same result in every iteration. Hence time limit exceeded 
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        import sys
        if len(nums) == k:
            return sum(nums)/k
        else:
            max_avg = -(sys.maxsize)
            for i in range(0,len(nums)-k+1):
                new_avg = sum(nums[i:i+k])/k
                if new_avg > max_avg:
                    max_avg = new_avg
            return max_avg


# Solution-2 - Optimized approach - TC=O(n)
'''
Sliding window problem
if len(nums) == k return sum(nums)/k as result. else loop through nums list from 0 to len(nums)-k+1.
Algorithm steps
    1. First calculate sum of elements from 0 to k index as prev_sum
    2. In every iteration, calculate (prev_sum - nums[i-1] + nums[i+k-1]). subtract last index and add next index value
    3. Calculate new_avg using prev_sum and check the max condition
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = sum(nums[0:k])/k
        prev_sum = sum(nums[0:k])
        for i in range(1,len(nums)-k+1):
            prev_sum = prev_sum-nums[i-1]+nums[i+k-1]
            new_avg = prev_sum/k
            if new_avg > max_avg:
                max_avg = new_avg
        return max_avg