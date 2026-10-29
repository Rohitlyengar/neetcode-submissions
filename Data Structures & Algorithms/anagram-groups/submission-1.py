class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            index[tuple(count)].append(s)
        return list(index.values())
