class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def DFS(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = DFS(i + 1, not buying) - prices[i]
                cooldown = DFS(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = DFS(i + 2, not buying) + prices[i]
                cooldown = DFS(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return DFS(0, True)
