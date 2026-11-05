class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        def DFS(crs: int) -> bool:
            if crs in visit:
                return False

            if preMap[crs] == []:
                return True

            visit.add(crs)

            for pre in preMap[crs]:
                if not DFS(pre):
                    return False
            preMap[crs] = []
            visit.remove(crs)

            return True
        
        
        for crs in range(numCourses):
            if not DFS(crs):
                return False
        return True

