class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        net = 0
        for i in range(1,n):
            prof = max(0,prices[i]-prices[i-1])
            net += prof
        return net

        