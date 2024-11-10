'''
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.

For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
'''

# Solution-1: 
'''
Algorithm:
    1. Find the frequency of each char in both words
    2. check each char of word1 present in word2, if not return false
    3. Next, we need to compare only frequency values irrespective of char, and sort them and compare if both are equal ot not 

Time Complexity = O(NlogN)
Space Complexity = O(N)
    
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter

        d1 = Counter(word1)
        d2 = Counter(word2)

        s1 = set(word1)
        s2 = set(word2)
        for ele in s1:
            if ele not in s2:
                return False
        l1 = [v for k, v in d1.items()]
        l2 = [v for k, v in d2.items()]
        if sorted(l1) == sorted(l2):
            return True
        else:
            return False