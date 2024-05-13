# Solution using Kadane's algorithm if else approach

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if (price < min_price):
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))