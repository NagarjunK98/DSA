'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Input: s = "a##c", t = "#a#c"
Output: true
'''

# Solution-1: Stack implementation. TC=O(N) & SC=O(N)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            l = []
            for i in s:
                if i == '#':
                    if len(l) == 0:
                        continue
                    else:
                        l.pop()
                else:
                    l.append(i)
            
            return "".join(l)
    
        return process_string(s) == process_string(t)