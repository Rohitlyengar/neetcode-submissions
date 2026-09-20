class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def DFS(i, curr):
            if curr == target:
                res.append(subset[:])
                return
            
            if i >= len(nums) or curr > target:
                return
            
            subset.append(nums[i])
            DFS(i, curr + nums[i])

            subset.pop()
            DFS(i + 1, curr)
        
        DFS(0, 0)
        return res
