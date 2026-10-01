class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        for num in nums:

            if num - 1 in nums:
                continue

            curr = 1
            next = num + 1

            while next in nums:
                curr += 1
                next = next + 1
            res = max(res, curr)
        return res
