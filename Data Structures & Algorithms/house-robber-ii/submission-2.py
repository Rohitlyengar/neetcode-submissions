class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robbery(nums[1:]), self.robbery(nums[:-1]), nums[0])
    
    def robbery(self, nums: List[int]) -> int:
        nums.append(0)

        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i + 1], nums[i] + nums[i + 2])
        return nums[0]
        