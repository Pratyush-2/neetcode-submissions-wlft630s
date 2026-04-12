class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        r = 1
        max_profit = 0 
        while r < n:
            if prices[l] > prices[r]:
                l = r
                
            elif prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit,profit)
            r+=1
        return max_profit
                

                


        