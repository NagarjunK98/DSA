'''
Given two integer arrays nums1 and nums2, return an array of their 
intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
# Solution-1 : 2 pointer approach. TC=O(NlogN) & SC=O(1). Sorting is involved
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        s = set()
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                s.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return s


# Solution-2: Hash table approach. Sorting not involved. TC=O(N) SC=O(N)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        d2 = dict()
        for ele in nums1:
            if ele not in d1:
                d1[ele] = 1
        for ele in nums2:
            if ele not in d2:
                d2[ele] = 1
        res = []
        if len(d1) < len(d2):
            for ele in d1:
                if ele in d2:
                    res.append(ele)
        else:
            for ele in d2:
                if ele in d1:
                    res.append(ele)  
        return res 

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

# Solution-1 : 2 pointer approach. TC=O(NlogN) SC=(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return res

# Solution-2: Counter approach(hash table). TC=O(n+m) SC=O(n+m)
# https://www.geeksforgeeks.org/python-counter-objects-elements/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return ((c1 & c2).elements())

'''
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
Answer: Instead of using extra space for creation hashmap for each array we can use Two Pointers or Binary Search approaches

What if nums1's size is small compared to nums2's size? Which algorithm is better?
Answer: Answer: Binary Search approach will works better than Two pointers, because we don't need to traverse between all second array for finding element. We can juse do int in "log time"

What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
Answer: So we can use Binary Search approach to be able make more efficient operations on memory disk.
'''