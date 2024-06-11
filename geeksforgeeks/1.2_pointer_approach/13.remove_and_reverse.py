'''
Given a string S which consists of only lowercase English alphabets, you have to perform the below operations:
If the string S contains any repeating character, remove the first repeating character and reverse the string and again perform the above operation on the modified string, otherwise, you stop.
You have to find the final string.

Input: S = "abab"
Output: ba
Explanation:
In 1st operation: The first repeating character is a. After Removing the first character, S = "bab". After Reversing the string, S = "bab".
In 2nd operation: The first repeating character is b. After Removing the first character, S = "ab". After Reversing the string, S = "ba". Now the string S does not contain any repeating character.

Input: S = "dddd"
Output: d
Explanation:
In 1st operation: The first repeating character is d. After Removing the first character, S = "ddd". After Reversing the string, S = "ddd". 
In 2nd operation: Similarly, S="dd".
In 3rd operation: Similarly, S="d". Now the string S does not contain any repeating character.

Input: S = "dcdbeada"
Output: daebc
'''
# Solution - 1 First approach - Time limit exceeded (1110/1115) test cases
'''
Algo steps:
    1. First the number of occurances of each char using counter 
    2. convert string to list and init i=0
    3. loop through list till i < len(l)
        3.1 if counter[char] > 1 then decrement counter, remove char, reverse list and assign i=0
        3.2 Else i+=1
    4. return "".join(l) as final string
'''
class Solution:
    def removeReverse(self, S): 
        from collections import Counter
        
        counter = Counter(S)
        l = list(S)
        i = 0
        while i < len(l):
            if counter[l[i]] > 1:
                counter[l[i]] -= 1
                l.remove(l[i])
                l = l[::-1]
                i = 0
            else:
                i+=1
        return "".join(l) 