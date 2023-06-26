'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

# Solution-1:
'''
Using linear search or brute force technique
Time Complexity = O(n2)
Space Complexity = O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)-1):
            f=0
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    l.append(i)
                    l.append(j)
                    f=1
                    break
            if f==1:
                break
        return l
        
# Solution-2: 
'''
Using hashmap or dictionary
Time Complexity = O(n)
Space Complexity = O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in d and d[y]!=i:
                return i, d[y]

# Solution-3: 
'''
Using sorting technique and 2-pointer approach
Time Complexity = O(n*logn) => Sorting(O(nlogn)) + search(O(n)) => O(nlogn)
Space Complexity = O(n)
'''
class Solution:

    def sort_by_first_ele(self, l: List[int]) -> List[int]:
        l.sort(key = lambda x:x[0])
        return l

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            l.append([nums[i], i])
        
        sorted_list = self.sort_by_first_ele(l)
        start = 0
        end = len(sorted_list) - 1
        
        while start < end:
            if(sorted_list[start][0]+ sorted_list[end][0] == target):
                return sorted_list[start][1],sorted_list[end][1]
            elif(sorted_list[start][0]+ sorted_list[end][0] < target):
                start = start + 1
            elif(sorted_list[start][0]+ sorted_list[end][0] > target):
                end = end - 1