'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
# Solution-1 - First approach - https://www.geeksforgeeks.org/a-product-array-puzzle/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # allocate memory for temp array
        left_array = [0]*n
        right_array = [0]*n
        # allocate memory for result array
        res = [0]*n

        # Initialize left[0] & right[n-1] = 1
        left_array[0] = 1
        right_array[n-1] = 1

        for i in range(1,n):
            left_array[i] = left_array[i-1] * nums[i-1]

        for j in range(n-2,-1,-1):
            right_array[j] = right_array[j+1] * nums[j+1]
        
        for i in range(n):
            res[i] = left_array[i] * right_array[i]
        return res


'''
Same problem, instead of product do addition of all elements except itself
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # allocate memory for temp array
        left_array = [0]*n
        right_array = [0]*n
        # allocate memory for result array
        res = [0]*n

        # Initialize left[0] & right[n-1] = 0
        left_array[0] = 0
        right_array[n-1] = 0

        for i in range(1,n):
            left_array[i] = left_array[i-1] + nums[i-1]
            
        for j in range(n-2,-1,-1):
            right_array[j] = right_array[j+1] + nums[j+1]
        
        for i in range(n):
            res[i] = left_array[i] + right_array[i]
        return res