'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
'''

# Solution-1 - First approach - Variable length sliding window approach(Solution is same as maximum consecutive ones III problem)
'''
Keep track of number of zeros and it should be <= 1 else move the left window index
Algo steps:
    1. Init l & r to 0 index, num_zeros=0, and max_one_len=0
    2. loop from 0 to len(nums) using r, check if ele is 0 then increment num_zeros by 1
    3. Also check if num_zeros > 1 then move l index forward and if nums[l]=0, decrement num_zeros by 1
    4. In every iteration, find max(prev_max, r-l)

TC=O(N)
SC=O(1)
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        num_zeros = 0
        max_one_len = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros +=1
            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            m = r -l
            max_one_len = max(max_one_len, m)
        print(r,l)
        return max_one_len