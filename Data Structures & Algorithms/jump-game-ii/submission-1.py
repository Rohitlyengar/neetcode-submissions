class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0

        l = 0
        r = 0
        while r < len(nums) - 1:
            maximum = 0
            for i in range(l, r + 1):
                if nums[i] + i > maximum:
                    maximum = nums[i] + i
            res += 1
            l = r + 1
            r = maximum
        return res
