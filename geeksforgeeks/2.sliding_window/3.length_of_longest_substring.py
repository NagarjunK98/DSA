'''
Given a string S, find the length of the longest substring without repeating characters.

Input:
S = "geeksforgeeks"
Output: 7
Explanation: Longest substring is "eksforg".

Input:
S = "abdefgabef"
Output: 6
Explanation: Longest substring are "abdefg" , "bdefga" and "defgab".

You don't need to take input or print anything. Your task is to complete the function longestUniqueSubsttr() which takes a string S as and returns the length of the longest substring.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(K) where K is constant.
'''

# Solution-1 First approach
'''
Algo steps:
    1. Init low=0, high=0, length=0
    2. Maintain an ordered dict to track ele in order to check repeat char with index
    3. if ele not in dict add ele with index
    4. If ele in dict
        4.1 find max(length, high-low)
        4.2 point the low index to d[ele]+1 as new starting point
        4.3 delete all k,v pair from dict till that repeat char and add new ele to end of dict
    5. find max(length, high-low) to handle no repeat char or find max of last instance of string
    5. return length

TC=O(nlogn)
SC=O(n)
'''
class Solution:
    def longestUniqueSubsttr(self, S):
        from collections import OrderedDict
        low = 0
        high = 0
        length = 0
        d = OrderedDict()

        while high < len(S):
            ele = S[high]
            if ele not in d:
                d[ele] = high
            else:
                length = max(length, high-low)
                low = d[ele]+1
                keys = []
                for k,v in d.items():
                    if k != ele:
                        keys.append(k)
                    else:
                        keys.append(k)
                        break
                for ele in keys:
                    del d[ele]
                
                d[S[high]] = high
            high += 1
        length = max(length, high-low)
        return length