'''
Given two strings, find if we can make first string from second by deleting some characters from second and rearranging remaining characters.

Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : Not Possible

Input : s1 = GeeksforGeeks
      : s2 = rteksfoGrdsskGeggehes
Output : Possible
'''

# Solution-1: Using counter approach
'''
1. First find occurances of each char in both strings
2. Find intersection of both char counts
3. check intersection is matching with occurances of string-1
'''
from collections import Counter

c1 = Counter(s1)
c2 = Counter(s2)

intersection = c1 & c2

if intersection == c1:
    print("possible")
else:
    print("Not possible")