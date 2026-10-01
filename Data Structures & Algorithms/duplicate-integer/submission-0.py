class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        index = set()

        for num in nums:
            if num in index:
                return True
            index.add(num)
        return False
        