#we are using two pointer approach.Fast and Slow (Tortoise and Hare)How it works: Both pointers start at the same location but move at different speeds or intervals.
#we will be comparing first two,if it is falling down then move right pointer to right until the end with the max value
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #l is buy day and r is the sell day
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP