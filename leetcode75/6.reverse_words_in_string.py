'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
# Solution-1 - First approach with extra space O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        # remove extra spaces between words and leading & training spaces
        s = re.sub(" +", " ", s)
        l = s.split()
        low = 0
        high = len(l)-1
        while low < high:
            temp = l[low]
            l[low] = l[high]
            l[high] = temp
            low += 1
            high -= 1
        return " ".join(l)

# Solution-2 - Second approach with list reversal
class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        # remove extra spaces between words and leading & training spaces
        s = re.sub(" +", " ", s)
        l = s.split()
        return " ".join(l[::-1])