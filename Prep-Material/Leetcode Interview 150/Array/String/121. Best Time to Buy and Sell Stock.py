# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=1pkOgXD63yU

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxi = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxi = max(profit, maxi)
            else:
                l = r
            r += 1
        return maxi 