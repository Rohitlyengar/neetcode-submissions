class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        cache = {}

        def DFS(i: int, curr: int) -> bool:
            if curr == target:
                return True
            
            if i >= len(nums) or curr > target:
                return False
            
            cache[(i, curr)] = DFS(i + 1, curr + nums[i]) or DFS(i + 1, curr)
            return cache[(i, curr)]

        return DFS(0, 0)
        