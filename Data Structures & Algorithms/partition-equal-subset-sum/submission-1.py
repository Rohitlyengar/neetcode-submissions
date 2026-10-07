class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        index = set()
        index.add(0)

        for num in nums:
            for n in list(index):
                if n + num == target:
                    return True
                index.add(n + num)
        return False
