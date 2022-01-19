class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[i]
        peak = prices[i]
        maxProfit = 0

        while(i < len(prices) - 1) :
            while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i]
            while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):
                i += 1
            peak = prices[i]
            maxProfit = peak - valley
        return maxProfit