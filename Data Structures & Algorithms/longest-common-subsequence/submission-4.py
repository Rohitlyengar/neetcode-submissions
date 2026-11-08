class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def DFS(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + DFS(i + 1, j + 1)
            else:
                cache[(i, j)] = max(DFS(i + 1, j), DFS(i, j + 1))
            
            return cache[(i, j)]
        
        return DFS(0, 0)

