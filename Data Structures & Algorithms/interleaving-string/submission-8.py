class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}

        def DFS(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            elif i + j == len(s3):
                cache[(i, j)] = True
            elif i < len(s1) and s1[i] == s3[i + j] and DFS(i + 1, j):
                cache[(i, j)] = True
            elif j < len(s2) and s2[j] == s3[i + j] and DFS(i, j + 1):
                cache[(i, j)] = True
            else:
                cache[(i, j)] = False
            return cache[(i, j)]
        return DFS(0, 0)
