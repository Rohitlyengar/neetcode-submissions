class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, h = 0, len(height) - 1
        maxL, maxH = height[l], height[h]

        while l <= h:
            if maxL <= maxH:
                maxL = max(height[l], maxL)
                res += maxL - height[l]
                l += 1
            else:
                maxH = max(height[h], maxH)
                res += maxH - height[h]
                h -= 1
        return res
 