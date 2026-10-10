class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def DFS(i: int, curr: int) -> None:
            if curr == amount:
                return 1

            if i >= len(coins) or curr > amount:
                return 0

            if (i, curr) in cache:
                return cache[(i, curr)]

            cache[(i, curr)] = DFS(i, coins[i] + curr) + DFS(i + 1, curr)
            return cache[(i, curr)]
    
        return DFS(0, 0)
        