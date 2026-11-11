class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}

        for i, c in enumerate(s):
            index[c] = i
        
        res = []
        start = end = 0
        for i in range(len(s)):
            end = max(end, index[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = end + 1

        return res        
