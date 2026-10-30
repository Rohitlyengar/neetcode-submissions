class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in index:
                index.remove(s[l])
                l = l + 1
            
            res = max(res, (r - l + 1))
            index.add(s[r])
        return res
        