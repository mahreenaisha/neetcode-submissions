class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while (right < len(prices)):
            buy = prices[left]
            sell = prices[right]
            if (sell > buy):
                profit = sell - buy
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1

        return maxProfit

        