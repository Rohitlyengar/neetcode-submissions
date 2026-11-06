class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        index = defaultdict(list)

        for src, dest in edges:
            index[src].append(dest)
            index[dest].append(src)
        
        visit = set()
        def DFS(src: int, parent: int) -> None:
            if src in visit:
                return
            
            visit.add(src)

            for dest in index[src]:
                if dest == parent:
                    continue
                DFS(dest, src)
                    
        res = 0
        for src in range(n):
            if src not in visit:
                res += 1
                DFS(src, -1)
        return res
