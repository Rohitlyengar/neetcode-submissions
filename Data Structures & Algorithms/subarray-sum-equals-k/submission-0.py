class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0

        index = { 0 : 1 }

        for num in nums:
            sum += num

            if sum - k in index:
                res += index[sum - k]
            index[sum] = 1 + index.get(sum, 0)
        return res
