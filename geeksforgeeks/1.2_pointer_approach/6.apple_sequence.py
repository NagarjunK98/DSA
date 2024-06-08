'''
There is a string of size n containing only 'A' and 'O'. 'A' stands for Apple, and 'O' stands for Orange. We have m number of spells, each spell allows us to convert an orange into an apple.

Find the longest subarray of apples you can make, given a string and the value of m

Input:
N = 5
M = 1
arr[] = 'AAOAO'
Output: 4 
Explanation: Changing the orange at 
3rd position into an apple gives 
us the maximum possible answer.

Input:
N = 5
M = 1
arr = 'AOOAO'
Output: 2
Explanation: Changing any orange into 
an apple will give us a sequence 
of length 2.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function appleSequence() which takes the array in the form of a string, its size n, and an integer m as input parameters and returns the largest apple sequences after converting m oranges.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
'''

# Solution - 1 Optimized approach - 2 pointer or sliding window
'''
Keep track of number of oranges and it should be <= m else move the left window index
Algo steps:
    1. Init l & r to 0 index, orange_count=0, and max_apple_len=0
    2. loop from 0 to len(arr) using r, check if ele is 'O' then increment orange_count by 1
    3. Also check if orange_count > k then move l index forward and if nums[l]='O', decrement orange_count by 1
    4. In every iteration, find max(prev_max, r-l+1)

TC=O(N)
SC=O(1)
'''
class Solution:
    def appleSequences(self, n, m, arr): 
        l = 0
        max_apple_len = 0
        orange_count = 0
        for r in range(n):
            if arr[r] == 'O':
                orange_count += 1
            while orange_count > m:
                if arr[l] == 'O':
                    orange_count -= 1
                l+=1
            max_apple_len = max(max_apple_len, r-l+1)
        return max_apple_len