'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

# Solution-1
'''
Using sorting technique and 2-pointer approach
Time complexity: O(n3)
Space complexity: O(n)
'''
class Solution:

    def sort_list(self, l: List[int]) -> List[int]:
        l.sort()
        return l
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []
        nums = self.sort_list(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                start = j+1
                end = len(nums)-1
                while(start < end):
                    if(nums[i]+nums[j]+nums[start]+nums[end] == target):
                        if([nums[i], nums[j], nums[start], nums[end]]) not in l:
                            l.append([nums[i], nums[j], nums[start], nums[end]])
                        start = start+1
                    elif(nums[i]+nums[j]+nums[start]+nums[end] < target):
                        start = start+1
                    else:
                        end = end - 1
        return l