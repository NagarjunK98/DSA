'''
Geek wants to make a special space for candies on his bookshelf. Currently, it has N books, each of whose height is represented by the array height[] and has unit width.

Help him select 2 books such that he can store maximum candies between them by removing all the other books from between the selected books. The task is to find out the area between two books that can hold the maximum candies without changing the original position of selected books.

Input: N = 3, height[] = {1, 3, 4}
Output: 1
Explanation:
1. Area between book of height 1 and book of 
height 3 is 0 as there is no space between 
them.
2. Area between book of height 1 and book of 
height 4 is 1 by removing book of height 3.
3. Area between book of height 3 and book of 
height 4 is 0 as there is no space between them.

Input: N = 6, height[] = {2, 1, 3, 4, 6, 5}
Output: 8
Explanation: Remove the 4 books in the middle 
creating length = 4 for the candy dam. Height 
for dam will be min(2,5) = 2. 
Area between book of height 2 and book 
of height 5 is 2 x 4 = 8.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''
# Solution-1 First approach
'''
We need to maximize the width of list along with height. So start from first and last index
Algo steps:
    1. Init low=0 & high=n-1
    2. loop through the list, find max(max_area, (high-low-1)*min(a[low], a[high]))
    3. if a[low] < a[high] low++ else high--
    4. return max_area

TC=O(N)
SC=O(1)
'''
class Solution:
    def maxCandy(self, height, n): 
        low = 0
        high = n-1
        max_area = 0
        while low < high:
            max_area = max(max_area, (high-low-1)*min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area