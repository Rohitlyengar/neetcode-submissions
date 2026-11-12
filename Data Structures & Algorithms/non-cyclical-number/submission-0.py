class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        num = 0
        while True:
            while n:
                last = n % 10
                n = n // 10
                num += last ** 2
            
            if num in visit:
                return False
            elif num == 1:
                return True
            else:
                visit.add(num)
                n = num
                num = 0
