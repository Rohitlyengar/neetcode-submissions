class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def DFS(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == '#' or word[i] != board[r][c]:
                return False
            
            board[r][c] = '#'

            res = DFS(r + 1, c, i + 1) or DFS(r - 1, c, i + 1) or DFS(r, c - 1, i + 1) or DFS(r, c + 1, i + 1)

            board[r][c] = word[i]

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if DFS(r, c, 0):
                    return True
        return False
        