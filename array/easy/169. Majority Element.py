'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.


Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

# Solution-1:
'''
Using 2 pointer approach
Time Complexity = O(n)
Space Complexity = O(n)
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        c = 0
        v = nums[0]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]] + 1
                if d[nums[i]] > c:
                    v = nums[i]
                    c =  d[nums[i]]
        return v

# Solution-2:
'''
Using sorting and return n/2 element
Time Complexity = O(n)
Space Complexity = O(1)
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]