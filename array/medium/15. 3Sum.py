'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

# Solution-1
'''
Using sorting technique and 2-pointer approach
Time complexity: O(n2)
Space complexity: O(n)
'''
class Solution:

    def sort_list(self, l: List[int]) -> List[int]:
        l.sort()
        return l
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums = self.sort_list(nums)
        for i in range(len(nums)):
            ele = nums[i]
            start = i+1
            end = len(nums)-1
            while(start < end):
                if(nums[start]+nums[end]+ele == 0):
                    if [ele, nums[start], nums[end]] not in l:
                        l.append([ele, nums[start], nums[end]])
                    start = start + 1
                elif(nums[start]+nums[end]+ele < 0):
                    start = start + 1
                else:
                    end = end -1
        return l
