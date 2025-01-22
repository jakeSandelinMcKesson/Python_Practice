class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]
        sold = prices[0]

        for price in prices:
            if price < buy:
                buy = price
            
            if price - buy > 0 and price - buy > prof:
                prof = price -buy
        
        return prof