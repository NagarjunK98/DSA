'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49

Input: height = [1,1]
Output: 1
'''
# Solution-1 - First approach (2 pointer) TC O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value = min(height[0], height[-1])*(len(height)-1)
        low = 0
        high = len(height) - 1
        while low < high:
            new_max = min(height[low], height[high])*( high - low)
            if new_max > max_value:
                max_value = new_max
            if height[low] < height[high]:
                low+=1
            else:
                high-=1
        return max_value
