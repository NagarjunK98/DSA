'''
Given a string s, reverse the order of characters in each word within a sentence while still
preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        ll = []
        for i in l:
            ll.append(i[::-1])
        return " ".join(ll)