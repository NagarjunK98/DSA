'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        max_count = 0
        flag = True
        for i in s:
            if i not in d:
                d[i] = 1
                max_count = 1
            else:
                d[i] = d[i] + 1
                if d[i] > max_count:
                    max_count = d[i]
        
        for char, count in d.items():
            if count != max_count:
                flag = False
                break
        return flag