'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''

# Solution-1 : Brute Force Approach. TC=O(N2) - time limit exceeded
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

# Solution-2 : Linear approach with extra space. TC=O(N) &  SC=O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return nums[i] 
            
# Solution-3: 2 pointer approach. TC=O(NlogN) & SC=O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        fp = 0
        sp = 1
        n = len(nums)
        while fp < n and sp < n:
            if nums[fp] == nums[sp]:
                return nums[fp]
            else:
                fp += 1
                sp += 1
        