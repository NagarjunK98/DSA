'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

# Solution-1: Brute force
'''
Algorithm:
    1. count 0's,1's,2's
    2. replace from index=0

Time complexity = O(N+M)
Space complexity = O(C)    
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import OrderedDict

        d = OrderedDict()
        d[0] = 0
        d[1] = 0
        d[2] = 0

        for ele in nums:
            d[ele]+=1
        
        index = 0
        for k, v in d.items():
            for i in range(v):
                nums[index] = k
                index+=1


# Solution-2: Optimal solution 3 pointer approach
'''
Algorithm:
    1. Use 3 pointer low, mid and high. low -> track 0, mid -> track 1 and high -> track 2
    2. low to mid-1 -> 0, mid to high-1 -> 1 and mid -> high -> 2
    3. low till mid <= high, 
        if nums[mid] == 0 swap(mid, low) and low++, mid++ 
        if nums[mid]=1 mid++ 
        else swap(mid, high) high-1

Time complexity = O(N)
Space complexity = O(C)
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1