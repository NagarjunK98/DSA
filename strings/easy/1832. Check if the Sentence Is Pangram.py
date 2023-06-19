'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Input: sentence = "leetcode"
Output: false
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = list(sentence) # This method is used to split the string into list when delimiter is not present or known
        s = set(l)
        if len(s) == 26:
            return True
        else:
            return False