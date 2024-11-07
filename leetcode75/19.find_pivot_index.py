'''
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
'''

# Solution-1: prefix_sum
'''
Algorithm:
    1. Find sum of left elements index i in left array
    2. Find sum of right elements index i in right array in reverse order
    3. compare left array [i] == right array[i] return i else -1

Time complexity = O(N)
Space complexity = O(2N)
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = []
        right_sum = []
        left_cur_sum = 0
        right_cur_sum = 0

        for i in range(0, len(nums)):
            left_cur_sum += nums[i]
            right_cur_sum += nums[-i-1]
            left_sum.append(left_cur_sum)
            right_sum.append(right_cur_sum)

        pivot_index = -1
        for i in range(len(left_sum)):
            if left_sum[i] == right_sum[-i-1]:
                pivot_index = i
                break
        return pivot_index