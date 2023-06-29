'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
'''

# Solution - 1:
'''
Using sorting method
Time complexity: O(nlong)
Space complexity: O(1)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]] + 1
        
        # Sort the dict by value
        dict_sorted = sorted(d.items(), key = lambda x:x[1], reverse = True)
        # get k no of tuples from sorted list
        l = dict_sorted[:k]
        # extract values from tuples
        res = [t[0] for t in l]
        return res