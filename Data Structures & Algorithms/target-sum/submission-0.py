class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def DFS(i: int, curr: int) -> int:
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            
            if (i, curr) in cache:
                return cache[(i, curr)]
            
            cache[(i, curr)] = DFS(i + 1, curr + nums[i]) + DFS(i + 1, curr - nums[i])
            return cache[(i, curr)]
        
        return DFS(0 ,0)
