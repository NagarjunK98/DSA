'''
3194. Minimum Average of Smallest and Largest Elements

You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

Input: nums = [7,8,3,4,15,13,4,1]
Output: 5.5

Input: nums = [1,9,8,3,10,5]
Output: 5.5
'''
# Solution-1: 2 pointer. Sorting involved. TC=O(NlogN) & SC=O(1)
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_avg = (nums[0]+nums[-1])/2
        i = 1
        j = len(nums)-2

        while i < j:
            avg = (nums[i]+nums[j])/2
            i+=1
            j-=1
            if avg < min_avg:
                min_avg = avg
        return min_avg