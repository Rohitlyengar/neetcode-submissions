class Solution:
    def isPalindrome(self, s: str) -> bool:
        revStr = str()

        for c in s:
            if c.isalnum():
                revStr += c.lower()
        
        l = 0
        r = len(revStr) - 1

        while l <= r:
            if revStr[l] != revStr[r]:
                return False
            l += 1
            r -= 1
        return True
