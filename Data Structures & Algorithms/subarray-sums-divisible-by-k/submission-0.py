class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0

        index = defaultdict(int)
        index[0] = 1

        for num in nums:
            sum += num

            if sum % k in index:
                res += index[sum % k]
            index[sum % k] += 1
            
        return res