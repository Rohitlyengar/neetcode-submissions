class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xxor = n

        for i in range(len(nums)):
            xxor ^= i ^ nums[i]
        return xxor