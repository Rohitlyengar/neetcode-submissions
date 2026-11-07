class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def DFS(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                cache[(i, j)] = DFS(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(DFS(i + 1, j), DFS(i, j + 1), DFS(i + 1, j + 1))
            
            return cache[(i, j)]
        
        return DFS(0, 0)
