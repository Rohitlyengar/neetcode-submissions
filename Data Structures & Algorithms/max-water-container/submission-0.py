class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, l, r = 0, 0, len(heights) - 1

        while l <= r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            (l, r) = (l + 1, r) if heights[l] < heights[r] else (l, r - 1)
        return res
