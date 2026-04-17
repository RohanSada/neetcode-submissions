class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        max_profit = 0
        for r in range(len(prices)):
            if l == r:
                continue 
            if prices[r] < prices[l]:
                l = r
                continue
            diff = prices[r] - prices[l]
            max_profit = max(diff, max_profit)
        return max_profit 

        