'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number 
is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
'''

# Solution-1:
'''
Using 2 pointer approach
Time Complexity = O(n)
Space Complexity = O(1)
'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            f0 = 0
            f1 = 1
            for i in range(2,n+1):
                temp = f0+f1
                f0 = f1
                f1 = temp
            return f1
