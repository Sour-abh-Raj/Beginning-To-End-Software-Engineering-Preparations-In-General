# Solution using Kadane's algorithm
# Kadane's algorithm is used to find the maximum subarray sum in an array
# In this case, we are finding the maximum difference between two elements in an array
# The difference between two elements is the profit
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        curr_min = prices[0]
        curr_max = prices[0]
        max_profit = 0
        for i in range(1, n):
            if (prices[i] < curr_min):
                curr_min = prices[i]
                curr_max = prices[i]
            elif (prices[i] > curr_max):
                curr_max = prices[i]
                max_profit = max(max_profit, curr_max - curr_min)
        return max_profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))
        