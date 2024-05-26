'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

# Solution-1 - First approach
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        low = 0
        high = len(s)-1

        while low < high:
            if s[low] in vowels and s[high] in vowels:
                s = s[:low] + s[high] + s[low+1:high] + s[low] + s[high+1:]
                low = low + 1
                high = high - 1
            else:
                if s[low] not in vowels:
                    low = low + 1
                if s[high] not in vowels:
                    high = high - 1   
        return s

