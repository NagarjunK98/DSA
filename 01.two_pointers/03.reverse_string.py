'''
541. Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
'''

# Solution-1 : 2 pointer approach. reverse inplace. TC=O(N) & SC=O(N)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        j = k-1 if k < n else n-1

        while i < n and j < n:
            sub = s[i:j+1]
            s = s[0:i] + sub[::-1] + s[j+1:]
            i = 2*k+i
            j = 2*k+j
            if j > n:
                j = n-1
        return s 