'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

# Solution-1 - Optimized approach  variable length sliding window problem 
'''
Keep track of number of zeros and it should be <= k else move the left window index
Algo steps:
    1. Init l & r to 0 index, num_zeros=0, and max_window_len=0
    2. loop from 0 to len(nums) using r, check if ele is 0 then increment num_zeros by 1
    3. Also check if num_zeros > k then move l index forward and if nums[l]=0, decrement num_zeros by 1
    4. In every iteration, find max(prev_max, r-l+1)

TC=O(N)
SC=O(1)
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_window_len = 0
        num_zeros = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            m = r - l + 1
            max_window_len = max(max_window_len, m)
        return max_window_len
