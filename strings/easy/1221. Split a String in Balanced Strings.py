'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
'''

# Maintain balance, if R, increment balance by 1 else decrement by -1. If balance is = 0, then increment max_no by 1
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_no = 0
        balance = 0
        for char in s:
            if char == 'R':
                balance = balance - 1 
            elif char == 'L':
                balance = balance + 1
            if balance == 0:
                max_no = max_no + 1
        return max_no