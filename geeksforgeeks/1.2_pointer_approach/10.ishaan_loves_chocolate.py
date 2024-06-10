'''
As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar that contains N chocolate squares. Each of the squares has a tastiness level which is denoted by an array A[].

Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first. 

Determine the tastiness level of the square which his sister gets

Input : arr[ ] = {5, 3, 1, 6, 9}
Output : 1
Explanation:
Initially: 5 3 1 6 9
In first step: 5 3 1 6
In Second step: 5 3 1
In Third step: 3 1
In Fourth step: 1
Return 1

Input : arr[ ] = {5, 9, 2, 6} 
Output :  2

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''
# Solution -1 First approach
'''
Since Ishaan has start eating from first or last. He choose whichever is larger in each iteration
Algo steps:
    1. Init low = 0 & high = n-1
    2. loop through list till low < high anc check arr[low] < high then decrement high else increment high
    3. return arr[low] 

TC = O(N)
SC = O(1)
'''
class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        low = 0
        high = n-1
        
        while low < high:
            if arr[low] < arr[high]:
                high -= 1
            else:
                low += 1
        return arr[low]