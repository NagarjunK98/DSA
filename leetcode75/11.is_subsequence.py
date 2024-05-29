'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

# Solution-1 - First approach TC O(n2)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        for i in range(len(s)):
            char = s[i]
            flag = False
            for j in range(k, len(t)):
                if char == t[j]:
                    k = j+1
                    flag = True
                    break
            if flag == True:
                continue
            else:
                return False
        return True
                
# Solution-2 - 2-pointer approach TC O(n)
'''
Check if fp == sp then forward both fp & sp else sp. Finally check if we covered all chars of s by len(s) == fp
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        fp = sp = 0
        while fp < len(s) and sp < len(t):
            if s[fp] == t[sp]:
                fp+=1
                sp+=1
            else:
                sp+=1
        return True if fp == len(s) else False
                