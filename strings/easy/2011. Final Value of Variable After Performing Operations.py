'''
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X 
after performing all the operations
'''

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_value = 0
        for op in operations:
            if op == "X++" or op == "++X":
                final_value=final_value+1
            else:
                final_value=final_value-1
        return final_value
        