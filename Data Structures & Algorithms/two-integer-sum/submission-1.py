class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index:
                return [index[diff], i]
            index[nums[i]] = i
