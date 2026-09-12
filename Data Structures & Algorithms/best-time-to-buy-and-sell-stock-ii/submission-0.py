class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cash = [0] * n
        hold = [0] * n
        cash[0] = 0
        hold[0] = -prices[0]
        for i in range(1, n):
            cash[i] = max(cash[i-1], hold[i-1] + prices[i])
            hold[i] = max(hold[i-1], cash[i-1] - prices[i])
        return cash[n-1]
        