'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Input: str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
Output: "TAUXX"
'''

# Solution-1 - first approach

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        min_word = str1 if len(str1) <= len(str2) else str2
        max_word = str1 if len(str1) > len(str2) else str2
   
        for i in range(len(min_word)):
            word = min_word[0:len(min_word)-i]
            if max_word == word * (len(max_word)//len(word)) and min_word == word * (len(min_word)//len(word)):
                gcd = word
                break
        return gcd

# Solution-2 - Using gcd function from math lib

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        else:
            from math import gcd
            return str1[:gcd(len(str1), len(str2))] # or return str2[:gcd(len(str1), len(str2))] - both give same result
