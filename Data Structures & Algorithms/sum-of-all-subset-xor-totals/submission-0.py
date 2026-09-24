class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def DFS(i, curr):
            nonlocal res
            if i >= len(nums):
                res += curr
                return

            DFS(i + 1, nums[i] ^ curr)
            DFS(i + 1, curr)

        DFS(0, 0)
        return res
