class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def DFS(i: int, curr: int) -> None:
            if curr == target:
                res.append(subset[:])
                return
            
            if i >= len(candidates) or curr > target:
                return
            
            subset.append(candidates[i])
            DFS(i + 1, curr + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            DFS(i + 1, curr)

        DFS(0, 0)
        return res

