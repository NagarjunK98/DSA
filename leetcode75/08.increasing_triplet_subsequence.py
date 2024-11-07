'''
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
'''

# Solution-1 - Learned approached after research (DP approach + search). SC O(n)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        smallest_ele = [None]*n
        largest_ele = [None]*n

        # Find the smallest element till that index starting from 0
        min_so_far = nums[0]
        for i in range(1, n):
            smallest_ele[i] = min_so_far
            if nums[i] < min_so_far:
                min_so_far = nums[i]
        
        # find the largest element till that index starting from n-1
        max_so_far = nums[n-1]
        for i in range(n-2, -1, -1):
            largest_ele[i] = max_so_far
            if nums[i] > max_so_far:
                max_so_far = nums[i]
        
        # find a triplet by comparing smallest & largest array to original array
        for i in range(1,n-1):
            if smallest_ele[i] is not None and smallest_ele[i] < nums[i] and largest_ele[i] is not None and largest_ele[i] > nums[i]:
                print(nums[i], smallest_ele[i],largest_ele[i])
                return True
        return False
    
''' Sample input & output
nums =[1,5,0,4,1,3]
smallest_ele = [None, 1, 1, 0, 0, 0] 
largest_ele = [5, 4, 4, 3, 3, None]
It has increasing subsequence (0,1,3)
'''

# Solution-2 - Simplest and optimized solution. TC = O(n) & SC = O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import sys
        first_ele = sys.maxsize
        second_ele = sys.maxsize

        for i in range(len(nums)):
            if nums[i] <= first_ele:
                first_ele = nums[i]
            elif nums[i] <= second_ele:
                second_ele = nums[i]
            else:
                return True
        return False