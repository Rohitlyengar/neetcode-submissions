class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        num = min(nums)
        sum = 0

        while num:
            last = num % 10
            num = num // 10
            sum += last
        
        if sum % 2:
            return 0
        return 1
