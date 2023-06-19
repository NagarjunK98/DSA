'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A"

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
'''

# Used hash-table to reduce time complexity by storing char count 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total_count = 0
        d = {} 
        for char in jewels:
            if char not in d:
                char_count = stones.count(char)
                total_count = total_count + char_count
                d[char] = char_count
            else:
                total_count = total_count + d[char]
        return total_count