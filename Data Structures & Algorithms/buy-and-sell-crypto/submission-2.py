class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(len(prices)):
            if l==r:
                continue
            if prices[l] > prices[r]:
                l = r
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        return max_profit


        