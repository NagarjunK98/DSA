'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

# Solution-1:
'''
Using 2 pointer approach
Time Complexity = O(n)
Space Complexity = O(1)
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[c]
                nums[c] = temp
                c = c + 1