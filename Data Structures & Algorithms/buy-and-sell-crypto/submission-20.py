class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        
        for n in range(len(prices)):
            for p in prices[n+1:]:
                if p - prices[n] > max_p:
                    max_p = p - prices[n]
        return max_p

            