class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xxor = len(nums)

        for i in range(len(nums)):
            xxor ^= i ^ nums[i]
        return xxor
