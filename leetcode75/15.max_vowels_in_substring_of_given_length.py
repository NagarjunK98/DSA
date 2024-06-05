'''
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''

# Solution-1 - First approach - Time limited exceeded
'''
Sliding window problem
Algo steps:
    1. Extract substring of length k
    2. counter character frequency using Counter module from collections
    3. Calculate sum of vowels frequency and apply max logic to find maximum vowels count
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        from collections import Counter
        vowels_count = 0
        for i in range(0,len(s)-k+1):
            substring = s[i:i+k]
            counter = Counter(substring)
            new_vowels_count = counter['a']+counter['e']+counter['i']+counter['o']+counter['u']
            if new_vowels_count > vowels_count:
                vowels_count = new_vowels_count
        return vowels_count 
    


# Solution-2 - Optimized approach TC=O(n)
'''
Sliding window problem
Algo steps:
    1. First find count of vowels of substring from 0 to k characters
    2. Loop through string from 1 to len(s)-k+1, and check if previous char is vowel or not and next char is vowel or not based on that add or subtract prev_vowels_count
    3. Compare prev_vowels_count & vowels_count and get maximum of them as result
'''
class Solution:
    def count_vowels(self, s:str) -> int:
        c = 0
        for char in s:
            if char in ('a', 'e', 'i', 'o', 'u'):
                c+=1
        return c
    
    def maxVowels(self, s: str, k: int) -> int:
        prev_vowels_count = self.count_vowels(s[0:k])
        max_vowels_count = prev_vowels_count
        for i in range(1,len(s)-k+1):
            if s[i-1] in ('a', 'e', 'i', 'o', 'u'):
                prev_vowels_count -= 1
            if s[i+k-1] in ('a', 'e', 'i', 'o', 'u'):
                prev_vowels_count += 1
            if prev_vowels_count > max_vowels_count:
                max_vowels_count = prev_vowels_count
        return max_vowels_count 