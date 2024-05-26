'''
1768. Merge Strings Alternately - 2 pointer problem of string

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters
'''

# Solution-1 : My first approach 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_word = word1 if len(word1) < len(word2) else word2
        final_word = "" 
        for i in range(len(min_word)):
            final_word = final_word + word1[i]+word2[i]
        if len(word1) < len(word2):
            final_word = final_word + word2[i+1:]
        else:
            final_word = final_word + word1[i+1:]
        return final_word


# Solution-2: Using zip
'''
list is used so that we can do join at the end and Also concatenating characters using += is usually inefficient

zip -> It is used to loop through all the characters of passed words till length of smallest word

Time complexity = O(m+n) => length of 2 words
Space complexity = O(m+n) 
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = []

        for a, b in zip(word1, word2):
            merged_word.append(a+b)
        
        merged_word.append(word1[len(word2):])
        merged_word.append(word2[len(word1):])

        return "".join(merged_word)