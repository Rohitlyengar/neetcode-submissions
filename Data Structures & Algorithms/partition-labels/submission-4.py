class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        index = {}

        for i, c in enumerate(s):
            index[c] = i
        
        start = end = 0
        for i, c in enumerate(s):
            if i > end:
                res.append(end - start + 1)
                start = i
            
            end = max(end, index[c])
        res.append(end - start + 1)

        return res


