'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
 However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
'''

# Solution-1:
'''
Time Complexity = O(n)
Space Complexity = O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if min < prices[i]:
                if i < len(prices)-1:
                    if prices[i] >= prices[i+1]:
                        profit = profit + (prices[i]-min)
                        min = prices[i]
                        i = i + 1
                    elif prices[i] < prices[i+1]:
                        profit = profit + (prices[i+1] - min)
                        min = prices[i+1]
                        i=i+1 
                else:
                    profit = profit + (prices[i]-min)
            elif min > prices[i]:
                min = prices[i]
        return profit

# Solution-2:
'''
Time Complexity = O(n)
Space Complexity = O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = profit + (prices[i]-prices[i-1])
        return profit