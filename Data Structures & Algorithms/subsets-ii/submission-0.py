class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def DFS(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            DFS(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            DFS(i + 1)
        DFS(0)
        return res
