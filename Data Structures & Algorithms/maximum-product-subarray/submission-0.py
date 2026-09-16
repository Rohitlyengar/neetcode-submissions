class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = max(nums)
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            curMin, curMax = min(curMin * num, curMax * num, num), max(curMin * num, curMax * num, num)
            res = max(res, curMax)
        return res
