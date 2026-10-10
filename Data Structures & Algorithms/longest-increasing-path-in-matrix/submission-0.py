class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        res = 0
        
        def DFS(r: int, c: int, prev: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = 1 + max(DFS(r + 1, c, matrix[r][c]), DFS(r - 1, c, matrix[r][c]), DFS(r, c + 1, matrix[r][c]), DFS(r, c - 1, matrix[r][c]))
            return cache[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, DFS(r, c, -1))
        return res
