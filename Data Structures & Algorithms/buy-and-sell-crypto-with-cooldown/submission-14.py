class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def DFS(i: int, buying: bool) -> int:
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            if i >= len(prices):
                return 0
            
            if buying:
                buy = DFS(i + 1, not buying) - prices[i]
                cooldown = DFS(i + 1, buying)
                cache[(i, buying)] = max(buy, cooldown)
            else:
                sell = DFS(i + 2, not buying) + prices[i]
                cooldown = DFS(i + 1, buying)
                cache[(i, buying)] = max(sell, cooldown)
            
            return cache[(i, buying)]
        
        return DFS(0, True)
