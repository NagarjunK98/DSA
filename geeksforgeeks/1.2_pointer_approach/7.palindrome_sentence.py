'''
Given a single sentence s, check if it is a palindrome or not. Ignore white spaces and any other character you may encounter.

Input:
s = race car.
Output: 1 
Explanation: processing str gives us
"racecar" which is a palindrome.

Input:
s = hello world.
Output: 0
Explanation: processing str gives us
"helloworld" which is not a palindrome.

Your Task:  
You dont need to read input or print anything. Complete the function sentencePalindrome() which takes a string s as input parameter and returns a boolean value denoting if sentence is a palindrome or not.

Note: The driver code prints 1 if the returned value is true, otherwise 0.


Expected Time Complexity: O(N) where N is length of s.
Expected Auxiliary Space: O(1)
'''

# Solution -1 First approach
'''
Algo steps:
    1. Init l=0 & r=len(s)-1 and flag=1
    2. loop through s till l < r and check if char is alpha or not based on that increment or decrement the l & r index

TC = O(N)
SC = O(1) 
'''
class Solution:
    def sentencePalindrome(self, s):
        flag = 1
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                if s[l].lower() == s[r].lower():  # Optional: consider case insensitivity
                    l += 1
                    r -= 1
                else:
                    flag = 0
                    break
            if not s[l].isalpha():
                l += 1
            if not s[r].isalpha():
                r -= 1
        
        return flag
