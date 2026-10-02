class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        index = {}

        for num in nums:
            index[num] = 1 + index.get(num, 0)
        
        nums.sort(key = lambda num : (index[num], -num))

        return nums
