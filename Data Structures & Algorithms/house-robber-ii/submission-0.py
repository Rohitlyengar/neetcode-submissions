class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robbery(nums[1:]), self.robbery(nums[:-1]))
        
    def robbery(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for num in nums:
            temp = max(rob1, rob2 + num)
            rob2 = rob1
            rob1 = temp
        return rob1
