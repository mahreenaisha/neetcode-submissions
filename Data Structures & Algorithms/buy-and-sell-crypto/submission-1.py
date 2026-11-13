class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # tc = o(n), sc = o(1)
        # don't start right from the right most end as the sell day could be the second day
        left, right = 0, 1
        maxProfit = 0
        while (right < len(prices)):
            if (prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit
            