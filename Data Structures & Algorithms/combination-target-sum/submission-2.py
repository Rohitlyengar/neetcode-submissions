class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def DFS(i: int, curr: int) -> None:
            if i >= len(nums) or curr > target:
                return
            
            if curr == target:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            DFS(i, nums[i] + curr)

            subset.pop()
            DFS(i + 1, curr)
        
        DFS(0, 0)
        return res
        