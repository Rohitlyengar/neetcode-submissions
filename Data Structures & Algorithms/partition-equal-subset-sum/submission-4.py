class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for num in nums:
            for n in list(dp):
                if num + n == target:
                    return True
                dp.add(num + n)
        return False
        