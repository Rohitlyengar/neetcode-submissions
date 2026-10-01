class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index:
                return [index[diff], i]
            index[num] = i
        return -1
