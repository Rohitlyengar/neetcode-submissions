class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robbery(nums[1:]), self.robbery(nums[:-1]), nums[0])
    
    def robbery(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1, num + rob2)
            rob2 = rob1
            rob1 = temp
        return rob1
