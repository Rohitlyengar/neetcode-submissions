class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        cache = {}

        def DFS(i: int, curr: int) -> None:
            nonlocal res
            if (i, curr) in cache:
                return cache[(i, curr)]
                
            if curr == amount:
                return 1
            
            if i >= len(coins) or curr > amount:
                return 0 
            
            cache[(i, curr)] = DFS(i, curr + coins[i]) + DFS(i + 1, curr)
            return cache[(i, curr)]

        return DFS(0, 0)
