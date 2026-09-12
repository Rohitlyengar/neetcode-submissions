class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False] * 3

        for i in range(3):
            for triplet in triplets:
                if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                    continue
                
                if triplet[i] == target[i]:
                    res[i] = True
                    break
        return all(res)
