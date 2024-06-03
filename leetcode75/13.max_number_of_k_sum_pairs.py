'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
'''

# Solution -1 - First approach. Time Limit Exceeded
''' 
Take 1 element and search for (k-element) in the list. If found remove(element, (k-element)) till low < len(list)
TC=O(n2)
SC=O(1)
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        low = 0
        while low < len(nums):
            flag = False
            target = k - nums[low]
            for i in range(len(nums)):
                if nums[i] == target and i != low:
                    ops+=1
                    nums.remove(nums[low])
                    nums.remove(target)
                    flag = True
                    break
            if flag == False:
                low+=1
        return ops

# Solution-2 - 2 pointer approach TC=O(nlogn)
'''
First sort the list. initialize 2 pointer low & high. loop through till low < high
sort = O(nlogn)
loop = O(n)
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        low = 0
        high = len(nums)-1
        nums.sort()
        while low < high:
            target = k - nums[low]
            if target == nums[high]:
                ops+=1
                low+=1
                high-=1
            elif target > nums[high]:
                low+=1
            else:
                high-=1 
        return ops

# Solution-3 - Optimized approach(Not 2 pointer approach). No sorting needed
'''
Use defaultdict to track of (k-ele) count in the form of dict. 
If any list ele is found in tracking defaultdict, op++ else calculate(k-ele) if ele < k and increment tracking[k-ele] by 1
return ops
TC = O(n) - single pass
SC = o(n)
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        # Initialize defaultdict with integer. If key not found, it returns 0 and won't through key not found error
        track = defaultdict(int)
        ops = 0

        for ele in nums:
            if track[ele] > 0:
                ops += 1
                track[ele] -= 1
            elif ele < k:
                target = k - ele
                track[target] += 1
        return ops